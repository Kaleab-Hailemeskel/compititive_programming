class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_mul = [1] * (n + 1)
        postfix_mul = [1] * (n + 1)
        for i in range(1, n + 1):
            prefix_mul[i] = prefix_mul[i - 1] * nums[i - 1]
            
        for i in range(-2, -n - 2, -1):
            postfix_mul[i] = postfix_mul[i + 1] * nums[i + 1]
        
        for i in range(n):
            nums[i] = prefix_mul[i] * postfix_mul[i + 1]
       
        return nums
