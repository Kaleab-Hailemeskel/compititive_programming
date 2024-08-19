class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(index, li, size_):
            if len(li) == size_:
                ans.append(li[:])
                return
            
            for i in range(index, n):
                li.append(nums[i])
                backtrack(i + 1, li, size_)
                li.pop()
        
        for size in range(n + 1):
            backtrack(0, [], size)
        
        return ans
            
