class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            visited.add((row, col))
            
            for add_row, add_col in direction:
                new_row, new_col = row + add_row, col + add_col
                if inbound(new_row, new_col) and grid[new_row][new_col] == '1' and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count
            
            
            
            
