class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        check = set()
        for i in range(len(nums)):
            cycle_check = set()
            while True:
                if i in cycle_check: return True
                cycle_check.add(i)
                check.add(i)
                pre, i = i , (i + nums[i]) % len(nums)
                
                if pre == i or (nums[i] < 0 != nums[pre] > 0):
                    break
        return False
            
                
            
