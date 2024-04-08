class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        size = len(nums)
        ans = []
        for i in range(size):
            if nums[i] == target:
                ans.append(i)
            elif( nums[i] > target):
                break
        return ans
