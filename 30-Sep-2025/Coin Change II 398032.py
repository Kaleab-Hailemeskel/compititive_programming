# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        size = amount
        memo = [0] * (size + 1)
        memo[0] = 1
        coins.sort()
        for note in coins:
            for curr_amount in range(1, amount + 1):
                if curr_amount - note >= 0:
                    memo[curr_amount] += memo[curr_amount - note]
                  
        
        return memo[amount]