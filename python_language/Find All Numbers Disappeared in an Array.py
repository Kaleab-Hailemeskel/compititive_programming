class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        start = 0
        ans = []
        for i in range(n):
            diff = nums[i] - start
            for dis in range(start + 1, start + diff):
                ans.append(dis)
            start = nums[i]
        for dis in range(start + 1, n + 1):
            ans.append(dis)
        return ans
                
            
            
                
            
            
            
                
                
