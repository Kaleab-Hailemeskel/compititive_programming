# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res = 0
        max_bit = 36
        for i in range(max_bit):
            curr_set, curr_non_set = 0, 0
            for val in nums:
                if val & (1 << i): 
                    curr_set += 1 
                else:
                    curr_non_set += 1
            
            tot_set_ij = curr_set * (curr_set + curr_non_set) + (curr_non_set * curr_set)
            tot_set_k = curr_set
            final = tot_set_ij * tot_set_k

            res |= ((final & 1) << i) 
        return res


        