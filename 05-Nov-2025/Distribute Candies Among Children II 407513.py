# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for a in range(min(limit, n) + 1):
            remain = n - a
            if remain > 2 * limit:
                continue
            
            res += min(limit - (remain - limit), remain) + 1
        
        return res