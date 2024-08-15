class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def is_prime(num):
            if num <= 1: return False
            if num <= 3: return True
            if num % 2 == 0 or num % 3 == 0:      return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        count_prime = set()
        for num in nums:
            
            if is_prime(num): 
                count_prime.add(num)
                continue
            for factor in range(2, num//2 + 1):
                if not (num % factor) and is_prime(factor):
                    count_prime.add(factor)
        
        return len(count_prime)
        
                    
                    
                    
                    
                
