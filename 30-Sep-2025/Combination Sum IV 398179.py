# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, coins: List[int], amount: int) -> int:
        size = amount
        memo = [0] * (size + 1)
        memo[0] = 1
        coins.sort()
        for curr_amount in range(1, amount + 1):
            for note in coins:
                if curr_amount - note >= 0:
                    memo[curr_amount] += memo[curr_amount - note]
                  
        
        return memo[amount]