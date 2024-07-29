class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * (n + 1)
        for i, j , k in bookings:
            prefix_sum[i - 1] += k
            prefix_sum[j] -= k
        
        ass = 0
        for i in range(n):
            ass += prefix_sum[i]
            prefix_sum[i] = ass
        
        prefix_sum.pop()
        return prefix_sum
            
            
