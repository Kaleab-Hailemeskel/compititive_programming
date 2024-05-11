class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        kSum = sum(nums[:k])
        i , j = 0, k
        size = len(nums)
        max_ = kSum
        while j < size:
            kSum -= nums[i]
            kSum += nums[j]
            max_ = max(max_, kSum)
            j += 1
            i += 1

        return (max_ / k)
