class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = []
        for i in range(size):
            totMin = size
            for j in range(size):
                if nums[i] <= nums[j]:
                    totMin -= 1
            ans.append(totMin)

        return ans
