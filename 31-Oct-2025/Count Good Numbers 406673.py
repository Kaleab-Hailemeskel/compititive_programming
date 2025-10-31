# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        count_even_numbers = len([0, 2, 4, 6, 8])
        count_prime_numbers = len([2, 3, 5, 7])
        MOD = (10 ** 9) + 7
        even_count = math.ceil(n / 2)
        odd_count = n - even_count
        
        return (pow(count_even_numbers, even_count, MOD) * pow(count_prime_numbers, odd_count, MOD)) % MOD
        
        
