# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for t_index in range(n, -1, -1):
            for s_index in range(m, -1, -1):
            
                if t_index == n:
                    dp[t_index][s_index] = 1
                elif s_index == m:
                    dp[t_index][s_index] = 0
                else:
                    if s[s_index] == t[t_index]:
                        dp[t_index][s_index] = dp[t_index + 1][s_index + 1]
                    dp[t_index][s_index] += dp[t_index][s_index + 1]
  
        return dp[0][0]