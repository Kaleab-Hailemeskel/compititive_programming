# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        true, false, none = range(3)
        dp = [[none] * 2001 for _ in range(2001)]
        def recur(index, jump):
            if index == len(stones) - 1:
                return true
            
            if dp[index][jump] == none:
                dp[index][jump] = false
                for var in (-1, 0, 1):
                    next_stone = stones[index] + jump + var
                    next_index = bisect_left(stones, next_stone)
                    if next_index < len(stones) and stones[next_index] == next_stone:
                        dp[index][jump] = min(
                            dp[index][jump],
                            recur(next_index, jump + var)
                        )
            
            return dp[index][jump]
        
        return recur(0, 0) == true
               

