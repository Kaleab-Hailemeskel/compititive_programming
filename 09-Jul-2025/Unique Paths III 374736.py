# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        vis = set()
        n, m = len(grid), len(grid[0])
        num_empty = sum((val != -1) for line in grid for val in line)

        dxn = ((0, 1), (0, -1), (1, 0), (-1, 0))
        in_bound = lambda x, y: 0 <= x < n and 0 <= y < m
        
        
        
        def recur(row, col):
            res = 0
            if grid[row][col] == 2:
                return 1 if len(vis) == num_empty else 0

            for dx, dy in dxn:
                nx, ny = dx + row, dy + col
                if in_bound(nx, ny) and (nx, ny) not in vis and grid[nx][ny] != -1:    
                    vis.add((nx, ny))
                    res += recur(nx, ny)
                    vis.remove((nx, ny))
            return res
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    vis.add((row, col))
                    return recur(row, col)                    