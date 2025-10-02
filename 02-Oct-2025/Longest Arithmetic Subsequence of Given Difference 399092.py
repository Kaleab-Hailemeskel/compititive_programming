# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n = len(arr)
        memo = [1] * (n)
        val_i = {}
        for i in range(n - 1, -1, -1):
            val = arr[i]
            next_val = val + diff
            if next_val  in val_i:
                next_index = val_i[next_val] 
                memo[i] = memo[next_index] + 1
            val_i[val] = i
        return max(memo)