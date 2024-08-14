class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                index = nums[i]
                if index < n:
                    nums[index],nums[i] = nums[i], nums[index]
                else:
                    break
        for i in range(n):
            if i != nums[i]:
                return i
        return n
