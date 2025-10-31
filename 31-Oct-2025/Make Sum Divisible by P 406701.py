# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_dq = defaultdict(list)
        prefix = [0]
        prefix_dq[0].append(-1)
        cumul = 0

        for i, val in enumerate(nums):
            cumul = (cumul + val) % p
            prefix.append(cumul)

            prefix_dq[cumul].append(i)
        
        subt = prefix[-1]
        if subt == 0:
            return 0
        res = float('inf')
        for i in range(len(prefix) - 1, -1, -1):

            prefix_dq[prefix[i]].pop()
            if not prefix_dq[prefix[i]]: del prefix_dq[prefix[i]]
            wanted = (prefix[i] - subt) % p

            if wanted in prefix_dq:
                res = min(res, i - prefix_dq[wanted][-1])
        
        if res == float('inf') or res == len(nums) + 1:
            return -1 
        return res - 1
        
        
