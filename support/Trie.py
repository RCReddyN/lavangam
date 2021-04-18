word_list=[]    
try:
    from nltk.corpus import words
    word_list = words.words()
except:
    import nltk
    nltk.download('words')
    from nltk.corpus import words
    word_list = words.words()

def calc_dist(a, b):
    if a is None or len(a)==0:
        return len(b)
    if b is None or len(b)==0:
        return len(a)
    if a[len(a) -1] == b[len(b) -1]:
        return calc_dist(a[:len(a) -1],b[:len(b) -1])
    return 1 + min(calc_dist(a, b[:len(b)-1]),
    calc_dist(a[:len(a)-1], b),
    calc_dist(a[:len(a)-1], b[:len(b)-1]))


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
        if node.isWord and calc_dist(word, self.key) <= 7: 
            self.suggestion_list.append(word)
        for ch in node.children:
            word += ch
            self.suggestions(node.children[ch], word)
            word = word[0:len(word)-1]

    def suggestions_to_String(self):
        str_ = ''
        if len(self.suggestion_list) > 20:
            self.suggestion_list = self.suggestion_list[:7]
        for s in self.suggestion_list[:7]:
            str_ += s + '\n'
        ans = str_.strip()
        self.suggestion_list = []
        return ans