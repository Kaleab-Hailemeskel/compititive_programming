class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(num):
            if num<= 1 : return False
            if num <= 3: return True
            if num % 2 == 0 or num % 3 == 0:      return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        last_prime = -1
        min_dif = float('inf')
        ans = [-1, -1]
        for curr in range(left, right + 1):
            if isPrime(curr):
                if last_prime < 0: 
                    last_prime = curr
                else: 
                    if curr - last_prime < min_dif:
                        ans = [last_prime, curr]     
                        min_dif = curr - last_prime
                last_prime = curr
                
            if min_dif == 1:
                break
        return ans
