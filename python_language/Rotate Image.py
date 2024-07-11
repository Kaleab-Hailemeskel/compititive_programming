class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for m in range(n, 0, -1):
            for j in range((n - m), n):
                matrix[n - m][j], matrix[j][ n - m] = matrix[j][n - m], matrix[n - m][j]
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
