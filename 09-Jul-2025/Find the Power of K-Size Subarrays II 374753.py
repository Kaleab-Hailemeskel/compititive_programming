# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        flaw = [0]
        for i in range(1, len(nums)):
            if nums[i] != 1 + nums[i - 1]:
                flaw.append(flaw[-1] + 1)
            else:
                flaw.append(flaw[-1])
        
        res = []
        for right in range(k - 1, len(flaw)):
            left = right - k + 1
            if flaw[right] - flaw[left] == 0:
                res.append(nums[right])
            else:
                res.append(-1)
        return res
