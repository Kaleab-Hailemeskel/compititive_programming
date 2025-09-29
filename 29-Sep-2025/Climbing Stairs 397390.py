# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.memo = {0:1, 1:1}
        pass
    def climbStairs(self, n: int) -> int:
        if not (n in self.memo):
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


        