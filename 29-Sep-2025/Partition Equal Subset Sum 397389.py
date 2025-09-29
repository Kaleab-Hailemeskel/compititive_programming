# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        tot = sum(nums)
        if tot % 2:
            return False
        def find_half(index, curr_sum):
            if curr_sum == tot // 2:
                return True
            if index >= len(nums) or curr_sum > tot // 2:
                return False
            if (index, curr_sum) not in memo:
                memo[(index, curr_sum)] = find_half(index + 1, curr_sum + nums[index]) or find_half(index + 1, curr_sum)

            return memo[(index, curr_sum)]
        return find_half(0, 0)