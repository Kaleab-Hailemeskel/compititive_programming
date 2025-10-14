# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.root = {}

        

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        curr_node['_end'] = None

    def search(self, word: str) -> bool:
        def recur(index, curr_node):
            if index >= len(word):
                return '_end' in curr_node

            if word[index] == '.':
                return any(recur(index + 1, next_node) for next_node in curr_node.values() if next_node != None)

            if word[index] not in curr_node:
                return False

            return recur(index + 1, curr_node[word[index]])
        return recur(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)