# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        search = set(wordDict)
        n = len(s)
        dp = [[None] * (n + 1) for _ in range(n + 1)]
        def recur(start, end):
            # print(start, end)
            if start >= len(s) or end >= len(s):
                return start == end

            if dp[start][end] == None:
                portion = s[start:end + 1]
                include = False
                if  portion in search:                    
                    # print('\t', start, end)
                    include = recur(end + 1, end + 1)

                    # checking to return quickly
                    if include:
                        dp[start][end] = include
                        return dp[start][end]

                exclude = recur(start, end + 1) 
                
                dp[start][end] = include or exclude
            return dp[start][end]
        
        return recur(0, 0)
            
            
        