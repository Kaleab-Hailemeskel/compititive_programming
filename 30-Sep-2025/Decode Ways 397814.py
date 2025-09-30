# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        for i, val in enumerate(s):
            if val == '0' and (i == 0 or s[i - 1] > '2'):
                return 0


        memo = [-1] * (len(s) + 1)
        
        def recur(index):
            if index >= len(s):
                return 1
            if s[index] == "0": 
                return 0
            if memo[index] == -1:
                memo[index] = recur(index + 1)
                if index < len(s) - 1:
                    next_state = s[index] + s[index + 1]
                    if len(next_state) <= 2 and next_state <= "26":
                        memo[index] += recur(index + 2)
            return memo[index]
        
        return recur(0)



