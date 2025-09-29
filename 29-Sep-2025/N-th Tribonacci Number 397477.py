# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:        
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n < 2:
            return tri[n]
        for _ in range(n - 3 + 1):
            tri.append(sum(tri))
            tri.pop(0)
        return tri[-1]

        