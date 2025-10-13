# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for start_index, val in enumerate(nums):
            curr_gcd = val
            for next_index in range(start_index, n):
                curr_gcd = math.gcd(curr_gcd, nums[next_index])
                if curr_gcd == k:
                    res += 1
                elif math.gcd(curr_gcd , k) != k:
                    break
        
        return res        