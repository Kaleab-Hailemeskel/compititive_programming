class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        k = len(matrix[0])
        if not matrix[0][0] <= target <= matrix[n - 1][k - 1]:
            return False
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[m][0]:
                r = m - 1
            elif matrix[m][-1] >= target >= matrix[m][0]:
                l = m
                break
            elif target > matrix[m][0]:
                l = m + 1
            else:
                return True
        
        row = l
        l, r = 0, k - 1
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1 
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False
            
