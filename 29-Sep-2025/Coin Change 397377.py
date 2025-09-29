# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # row_size = 12 + 1
        col_size = amount + 1
        memo = [float('inf')] * col_size 
        memo[0] = 0
        for num in range(1, amount + 1):
            memo[num] = min(memo[num - notes] + 1 if num - notes >= 0 else float('inf') for notes in coins)
        
        res = memo[amount]
        return res if res != float('inf') else -1