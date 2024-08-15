class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[j] = -nums[j]
        return ans
