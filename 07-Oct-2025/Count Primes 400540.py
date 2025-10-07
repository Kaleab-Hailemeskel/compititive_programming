# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:     
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        pr = [True] * (n)
        def seive(bound):
            pr[0] = pr[1] = False
            for num in range(2, bound):
                if pr[num]:
                    for next_mult in range(num * num, n, num):
                        pr[next_mult] = False
        seive(n)
        return sum(pr)
        


        