# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = {}
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr['_end'] = True

        def recur(curr_node):
            res = ''
            for key, value in curr_node.items():
                if key != '_end' and '_end' in value:
                    poss_min = key + recur(value)
                    if (len(poss_min) > len(res)) or (len(poss_min) == len(res) and poss_min < res):
                        res = poss_min
                            
            
            return res
        return recur(root)


                