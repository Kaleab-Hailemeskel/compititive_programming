# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        BUY, SELL = 0, 1
        dp = [[-1] * 2 for _ in range(len(prices))]
        def recur(index, option):
            if index >= len(prices):
                return 0
            if dp[index][option] == -1:
                if option == BUY:
                    dp[index][option] = max(
                        -prices[index] + recur(index + 1, SELL),
                        recur(index + 1, BUY)
                    )
                else:
                    dp[index][option] = max(
                        prices[index] - fee + recur(index + 1, BUY),
                        recur(index + 1, SELL)
                    )

            return dp[index][option]
        
        return recur(0, BUY)