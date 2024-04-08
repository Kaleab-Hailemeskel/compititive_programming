class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        colors = [0] * 3
        for i in range(size):
            colors[nums[i]] += 1
        j = 0
        for i in range(size):
            while colors[j] <= 0 and j < 3:
                j += 1
            nums[i] = j
            colors[j] -= 1
