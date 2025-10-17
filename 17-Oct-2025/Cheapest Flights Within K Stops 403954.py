# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:        
        prev = [float('inf')] * n
        prev[src] = 0
        
        for _ in range(k + 1):
            curr = prev[:]
            for fr, to, cost in flights:
                curr[to] = min(curr[to], prev[fr] + cost)
            prev = curr[:]
        
        return prev[dst] if prev[dst] != float('inf') else -1