# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curr_min = nums[0]
        for i in range(1, len(nums)):
            while stack and stack[-1][0] <= nums[i]:
                stack.pop()
            if stack and stack[-1][1] < nums[i]:
                return True
            
            stack.append([nums[i], curr_min])
            curr_min = min(curr_min, nums[i])
        
        return False
            
            