class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(1, size):
            if nums[ i -1 ] != 0 and nums[i - 1] == nums[i] :
                nums[i-1] *= 2
                nums[i] = 0
        ans = [0] * size
        lt, rt = 0, size - 1
        for i in range(0, size):
            if nums[i] != 0:
                ans[lt] = nums[i]
                lt += 1
            else:
                ans[rt] = nums[i]
                rt -= 1
        return ans
