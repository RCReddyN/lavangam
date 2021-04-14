import random
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.suggestion_list = []
        with open("support//wordcache.txt") as f:
            for line in f.readlines():
                self.insert(line.strip())

    def insert(self, word):
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

    def search(self, word):
        curr = self.root
        for i in range(len(word)):
            ch = word[i]
            if ch not in curr.children:
                self.suggestions(self.root, word[0:i])
                return False
            curr = curr.children[ch]
        if curr.isWord:
            return True
        self.suggestions(curr, word)
        return False
    
    def suggestions(self, node, word):
        if node.isWord:
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