# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def recur_rob(index):
            if index >= n:
                return 0
            if index not in memo:
                memo[index] = nums[index] + max(recur_rob(index + 2), recur_rob(index + 3))
            return memo[index]
        
        return max(recur_rob(0), 0 if len(nums) == 1 else recur_rob(1))

        