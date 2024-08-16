class Solution:
    def minSteps(self, n: int) -> int:
        count_steps = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                count_steps += i
                n //= i
            i += 1
        if n > 1: count_steps += n
            
        return count_steps
        
            
            
        
