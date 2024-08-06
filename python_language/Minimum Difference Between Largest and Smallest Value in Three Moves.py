class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)  
        if n < 5:
            return 0
        nums.sort()
        min_window = nums[-1] - nums[0]
        j = 0
        for i in range(n-4, n):
            min_window = min(min_window, nums[i] - nums[j])
            j += 1
        return min_window
