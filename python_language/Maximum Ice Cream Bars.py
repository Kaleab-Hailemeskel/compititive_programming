class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        if n == 0: return n
        sum_ = 0
        costs.sort()
        i = 0
        while i < n and sum_ < coins:
            sum_ += costs[i]
            i += 1
        return i - 1 if sum_ > coins else i
            
