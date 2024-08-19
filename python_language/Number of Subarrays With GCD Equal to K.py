class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_gcd = 0
        for size in range(n):
            for i in range(n - size):
                max_gcd = nums[i]
                for j in range(i + 1, i + size + 1):
                    max_gcd = gcd(max_gcd, nums[j])
                    if max_gcd == 1: break
                count_gcd += int(max_gcd == k)
                
        
        return count_gcd
                
                
            
                
            
            
            
