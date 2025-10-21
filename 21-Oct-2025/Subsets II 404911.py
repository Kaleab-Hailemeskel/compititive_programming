# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res_set = set()
        nums.sort()
        for choice in range(1 << len(nums)):
            choice_res = []
            for bit_place in range(len(nums)):
                if 1 << bit_place & choice:
                    choice_res.append(nums[bit_place])
            
            res_set.add(tuple(choice_res))
        
        return list(res_set)

