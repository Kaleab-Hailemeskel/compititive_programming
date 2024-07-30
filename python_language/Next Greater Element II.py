class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n # the key point here is to have the default value of -1
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                j = stack.pop()
                ans[j] = nums[i % n]
            
            stack.append(i % n)            
            
        return ans
