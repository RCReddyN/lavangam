from support import Trie as tr

class Lavangam:
    def __init__(self, key):
        self.key = key
    
    def read_key(self):
        return input()

    def search_word(self, trie):
        if(trie.search(self.key)):
            return('The word seems to be of correct spelling.')
        return "Did you mean? \n"+ trie.suggestions_to_String()

def main():
    word_key = input().strip()
    trie = tr.Trie()
    spellchecker = Lavangam(word_key)
    print(spellchecker.search_word(trie))

if __name__=="__main__":
    main()
