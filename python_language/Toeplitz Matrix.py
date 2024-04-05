class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row_index in range(0, len(matrix) - 1):
            for col_index in range(0, len(matrix[0]) - 1):
                if matrix[row_index][col_index] != matrix[row_index + 1][col_index + 1]:
                    return False
                
        return True
