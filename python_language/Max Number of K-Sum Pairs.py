class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        count = 0
        while l < r:
            sum_ = nums[l] + nums[r]
            if sum_ == k:
                count += 1
                l += 1
                r -= 1
            elif sum_ > k:
                r -= 1
            else:
                l += 1
        
        return count
