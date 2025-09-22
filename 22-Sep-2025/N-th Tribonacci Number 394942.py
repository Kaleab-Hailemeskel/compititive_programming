# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def __init__(self):
        self.memo = {0:0, 2:1, 1:1}
        pass
    def tribonacci(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.memo[n]


        