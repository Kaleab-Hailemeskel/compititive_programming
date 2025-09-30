# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
# bottom-up solution
    def maxProfit(self, prices: List[int]) -> int:
        BUY, SELL = 0, 1
        n = len(prices)
        dp = [[0] * 2 for _ in range(len(prices) + 2)]
        for i in range(n - 1, -1, -1):
            dp[i][BUY] = max(
                -prices[i] + dp[i + 1][SELL],
                dp[i + 1][BUY]
            )
            dp[i][SELL] = max(
                prices[i] + dp[i + 2][BUY],
                dp[i + 1][SELL]
            )
        return dp[0][BUY]

        