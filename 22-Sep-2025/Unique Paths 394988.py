# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, row: int, col: int) -> int:
        dp = [ [1] * col for _ in range(row) ]
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]
        
        
