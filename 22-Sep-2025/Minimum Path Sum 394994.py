# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # precomputing on the last row
        for i in range(row - 2, -1, -1):
            grid[i][-1] += grid[i + 1][-1]
        
        # precomputing on the last col
        for i in range(col - 2, -1, -1):
            grid[-1][i] += grid[-1][i + 1]

        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                grid[i][j] += min(grid[i][j + 1] , grid[i + 1][j])
        
        return grid[0][0]