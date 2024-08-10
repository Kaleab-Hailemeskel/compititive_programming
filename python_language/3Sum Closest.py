class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        close = float('inf')
        close_dis = 0
        for left in range(n):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            
            mid, right = left + 1, n - 1
            while mid < right:
                tot = nums[mid] + nums[right] + nums[left]
                tot_dis, close_dis = abs(tot - target), abs(close - target)
                if tot_dis < close_dis:
                    close = tot
                if tot < target:
                    mid += 1
                elif tot > target:
                    right -= 1
                else:
                    return tot
                    
        return close
            
                
        
