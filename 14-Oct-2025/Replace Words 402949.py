# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        curr_node['_end'] = None
    def smallest_ending_index(self, word):
        curr_node = self.root
        for index, char in enumerate(word):
            if char not in curr_node:
                return len(word)
            curr_node = curr_node[char]
            if '_end' in curr_node:
                return index + 1
        return len(word)
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        
        sentence_arr = sentence.split()
        res = []
        for word in sentence_arr:
            res.append(word[:self.smallest_ending_index(word)])
        return ' '.join(res)
        
