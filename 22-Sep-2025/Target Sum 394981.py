# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict()


        def recur(curr_sum, index):
            if index == len(nums): 
                if curr_sum == target:
                    return 1
                return 0
            
            if (curr_sum, index) not in memo:
                first_half = recur( (curr_sum + nums[index]), index + 1)
                second_half = recur( (curr_sum - nums[index]), index + 1)
                memo[(curr_sum, index)] = first_half + second_half
            
            return memo[(curr_sum, index)]

        return recur(0, 0)