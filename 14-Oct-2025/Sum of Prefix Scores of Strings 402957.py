# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node:
                curr_node[char] = {'count':0}
            curr_node = curr_node[char]
            curr_node['count'] += 1

    def count_prefix(self, word):
        curr_node = self.root
        res = 0
        for char in word:
            curr_node = curr_node[char]
            res += curr_node['count'] 
        return res

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        return [self.count_prefix(word) for word in words]


        