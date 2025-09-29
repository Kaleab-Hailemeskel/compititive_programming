# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        def recur(curr_index):            
            # dp for curr_index is not initialized i.e. dp[curr_index] == 0
            if dp[curr_index] == 0:
                dp[curr_index] = 1
                for next_index in range(curr_index + 1, len(nums)):
                    curr_value = nums[curr_index]
                    next_value = nums[next_index]
                    if curr_value < next_value:
                        dp[curr_index] = max(
                            dp[curr_index], 
                            recur(next_index) + 1, 
                        )
            return dp[curr_index]

        return max(recur(index) for index in range(len(nums)))
        