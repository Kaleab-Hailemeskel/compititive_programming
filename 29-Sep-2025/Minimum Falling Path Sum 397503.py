# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for row in range(n - 2, -1, -1):
            for col in range(n):
                min_res = float('inf')
                for add_col in (-1, 0, 1):
                    new_col = col + add_col
                    if 0 <= new_col < n:
                        min_res = min(
                            min_res, 
                            matrix[row][col] + matrix[row + 1][new_col]
                        )
                matrix[row][col] = min_res
        
        return min(matrix[0])