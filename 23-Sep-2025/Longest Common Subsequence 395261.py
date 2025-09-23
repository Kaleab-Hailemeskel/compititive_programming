# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def recur(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) not in dp:
                if text1[i] == text2[j]:
                    dp[(i, j)] = 1 + recur(i + 1, j + 1)
                    return dp[(i, j)]
                
                dp[(i, j)] = max(recur(i, j + 1), recur(i + 1, j))
                
            return dp[(i, j)]
        
        return recur(0, 0)