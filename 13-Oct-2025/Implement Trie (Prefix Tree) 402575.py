# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            char_index = ord(char) - ord('a')
            if char_index not in curr:
                curr[char_index] = {}
            curr = curr[char_index]
        curr['_'] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            char_index = ord(char) - ord('a')
            if char_index not in curr:
                return False
            curr = curr[char_index]
        return '_' in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            char_index = ord(char) - ord('a')
            if char_index not in curr:
                return False
            curr = curr[char_index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)