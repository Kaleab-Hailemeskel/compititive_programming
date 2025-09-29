# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[0] * (n + 1) for _ in range(n + 1)]
        
        def recur(left, right):
            if left > right:
                return 0
            if memo[left][right] != 0:
                return memo[left][right]
            
            memo[left][right] = max(
                piles[left] + min(
                    recur(left + 2, right), 
                    recur(left + 1, right - 1)
                ),
                piles[right] + min(
                    recur(left, right - 2),
                    recur(left + 1, right - 1)
                )
            )

            return memo[left][right]
        left, right = 0, n - 1
        
        recur(left, right)
        tot_sum = sum(piles)
        
        return tot_sum - memo[left][right] < memo[left][right]
        


