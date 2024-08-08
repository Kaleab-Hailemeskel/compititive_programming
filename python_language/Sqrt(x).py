class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            sq = mid ** 2           
            
            if sq > x:
                high = mid - 1
            elif sq < x:
                low = mid + 1
                ans = mid
            else:
                return mid
        return ans
        
