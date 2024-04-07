class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for col in range(0, len(matrix[0]) ):
            arr = []
            for row in range(0, len(matrix)):
                arr.append(matrix[row][col])
            ans.append(arr)
        return ans
