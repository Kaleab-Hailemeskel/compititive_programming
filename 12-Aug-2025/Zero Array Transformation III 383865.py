# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        prefix = [0] * (len(nums) + 1)
        queries.sort(key=lambda ele: (ele[0]))
        heap_right = []
        q_index = 0
        for i in range(len(nums)):
            while q_index < len(queries) and queries[q_index][0] == i:
                heappush(heap_right, -queries[q_index][1])
                q_index += 1
            
            while prefix[i] < nums[i] and heap_right and -heap_right[0] >= i:
                prefix[i] += 1
                prefix[-heappop(heap_right) + 1] -= 1
            if prefix[i] < nums[i]:
                return -1
            prefix[i + 1] += prefix[i]
        
        return len(heap_right)

            

                
                





        