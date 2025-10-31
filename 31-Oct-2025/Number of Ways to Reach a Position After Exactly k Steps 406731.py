# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if abs(startPos - endPos) % 2 != k % 2 or abs(startPos - endPos) > k:
            return 0
        MOD = 10 ** 9 + 7
        
        m = abs(startPos - endPos)
        m += ((k - m) // 2)
        
        return math.comb(k, m) % MOD