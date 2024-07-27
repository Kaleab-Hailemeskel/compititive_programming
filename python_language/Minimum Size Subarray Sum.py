class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sum_, l = 0, 0
        min_arr = n + 1
        for r in range(n):
            sum_ += nums[r]
            while l <= r and sum_ >= target:
                min_arr = min(min_arr, r - l + 1)
                sum_ -= nums[l]
                l += 1
        
        return min_arr if min_arr != n + 1 else 0
                
