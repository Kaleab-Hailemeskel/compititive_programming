class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        n = len(nums)
        for i in range(n):
            count[nums[i]] += 1
        curr_start = 0
        for i in range(3):
            for j in range(curr_start, curr_start + count[i]):
                nums[j] = i
            curr_start += count[i]
            
        
                
