class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if n - m < citations[m]:
                r = m - 1
            elif n - m > citations[m]:
                l = m + 1
            else:
                return citations[m]
        return n - l
                
                
