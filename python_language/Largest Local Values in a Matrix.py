class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(1, len(grid) - 1):
            arr = []
            for j in range(1, len(grid) - 1):
                max = 0
                size = i + 2
                sizej = j + 2
                for m in range(i - 1, size):
                    for k in range(j - 1, sizej):
                        if grid[m][k] > max:
                            max = grid[m][k]
                arr.append(max)
            ans.append(arr)
        return ans
