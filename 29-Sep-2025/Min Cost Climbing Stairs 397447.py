# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [float('inf')] * len(cost)
        def recur(index):
            if index >= len(cost):
                return 0
            if memo[index] != float('inf'):
                return memo[index]
            
            memo[index] = cost[index] + min(recur(index + 1), recur(index + 2))
            return memo[index]
        index = 0
        return min(recur(index), recur(index + 1))