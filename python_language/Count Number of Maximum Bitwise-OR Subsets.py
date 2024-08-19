class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_ = 0
        for num in nums: max_ |= num
        n = len(nums)
        def dfs(index, li, curr_or):
            count = 0
            for i in range(index, n):
                li.append(nums[i])
                count += dfs(i + 1, li, curr_or | nums[i])
                li.pop()
            
            return count + int(curr_or == max_)
        
        return dfs(0, [], 0)
            
            
