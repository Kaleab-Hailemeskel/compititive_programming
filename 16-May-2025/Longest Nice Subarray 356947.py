# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        bit_count = 0
        left = 0
        max_res = float('-inf')
        for right, val in enumerate(nums):
            while bit_count ^ val != bit_count | val and left < right:
                bit_count ^= nums[left]
                left += 1
            max_res = max(max_res, right - left + 1)
            bit_count ^= val
        
        return max_res
            
                 
        