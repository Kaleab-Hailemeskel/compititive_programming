# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        def dfs(start_index, remain_len, curr_res):
            nonlocal res
            if remain_len == 0:
                res += curr_res
                return
            for index in range(start_index, n):
                dfs(index + 1, remain_len - 1, curr_res ^ nums[index])
            
        for each_len in range(1, n + 1):
            dfs(0, each_len, 0)   
        
        return res


