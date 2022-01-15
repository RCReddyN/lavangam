from support import Trie as tr


class Lavangam:
    def __init__(self, key):
        self.key = key

    def read_key(self):
        return input()

    def search_word(self, trie):
        return trie.search(self.key)


def main():
    word_key = input().strip().lower()
    trie = tr.Trie()
    spellchecker = Lavangam(word_key)
    print(spellchecker.search_word(trie))


if __name__ == "__main__":
    main()
