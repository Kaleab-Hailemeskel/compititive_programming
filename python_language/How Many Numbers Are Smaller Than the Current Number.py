class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            small_nums = 0
            for j in range(n):
                if nums[i] > nums[j]:
                    small_nums += 1
            ans[i] = small_nums
        
        return ans
                    
