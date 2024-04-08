class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coinSum = 0
        ltIndex = 0
        rtIndex = len(piles) - 2
        while ltIndex < rtIndex:
            coinSum += piles[rtIndex]
            ltIndex += 1
            rtIndex -= 2
        return coinSum
