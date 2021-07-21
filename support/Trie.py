from operator import attrgetter

word_list=[]    
try:
    from nltk.corpus import words
    word_list = words.words()
except:
    import nltk
    nltk.download('words')
    from nltk.corpus import words
    word_list = words.words()

class Word:
    def __init__(self, word, dist):
        self.word = word
        self.dist = dist

def calc_dist(s1, s2):
    n = len(s1)
    m = len(s2)
    if n == 0:
        return m
    if m == 0:
        return n
    cache = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        cache[i][0] = i
    for j in range(m + 1):
        cache[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = 1 + min(cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1])
            if i >= 1 and j >= 1 and s1[i] == s2[j-1] and s1[i-1] == s2[j]:
                cache[i][j] = min(cache[i][j], cache[i-2][j-2] + 1)

    return cache[n][m]

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.key = ''
        self.suggestion_list = []
        for word in word_list:
            self.insert(word)

    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word):
        self.key = word
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in curr.children:
                self.suggestions(curr, word[0:i])
                return False
            curr = curr.children[ch]
        if curr.isWord:
            return True
        self.suggestions(curr, word)
        return False
    
    def suggestions(self, node, word):
        dist = calc_dist(word, self.key)
        if node.isWord and dist <= 7: 
            self.suggestion_list.append(Word(word, dist))
        for ch in node.children:
            word += ch
            self.suggestions(node.children[ch], word)
            word = word[0:len(word)-1]

    def suggestions_to_String(self):
        str_ = ''
        self.suggestion_list.sort(key=attrgetter('dist'))
        for s in self.suggestion_list[:7]:
            str_ += s.word + '\n'
        ans = str_.strip()
        self.suggestion_list = []
        return ans
