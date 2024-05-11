class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        countZ = 0
        maxSize = 0
        while right < len(nums):
            if not nums[right]:
                countZ += 1
            while countZ > k and left <= right:
                if nums[left] == 0:
                    countZ -= 1
                left += 1
            maxSize = max(maxSize, right - left + 1) 
                
            right += 1
        
        return maxSize
                
                
            
