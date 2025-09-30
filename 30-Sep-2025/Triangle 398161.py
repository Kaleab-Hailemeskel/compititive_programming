# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):

                val = triangle[row][col]
                
                left_lower_index, right_lower_index = col, col + 1
                left_value = right_value = float('inf')
                
                if left_lower_index >= 0:
                    left_value = triangle[row + 1][left_lower_index]
                if right_lower_index < len(triangle[row + 1]):
                    right_value = triangle[row + 1][right_lower_index]
                
                triangle[row][col] += min(left_value, right_value)
        return triangle[0][0]


