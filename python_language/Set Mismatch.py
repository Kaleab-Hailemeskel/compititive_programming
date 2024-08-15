class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        dup = n
        for i in range(n):
            while i + 1 != nums[i]:
                index = nums[i] - 1
                if nums[i] == nums[index]:
                    dup = nums[i]
                    break
                else:
                    nums[i], nums[index] = nums[index], nums[i]
        ans.append(dup)
      
        for i in range(n):
            if i + 1 != nums[i]:
                ans.append(i + 1)
                break
        
        return ans
