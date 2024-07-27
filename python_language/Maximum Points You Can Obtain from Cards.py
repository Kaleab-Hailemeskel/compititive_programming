class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total_k = 0
        n = len(cardPoints)
        l, r = 0, n - k
        for i in range(r, n):
            total_k += cardPoints[i]
        ans = total_k
        while r < n:
            total_k += (cardPoints[l] - cardPoints[r])
            ans = max(ans, total_k)
            l += 1
            r += 1
        
        return ans
        
        
            
        
        
