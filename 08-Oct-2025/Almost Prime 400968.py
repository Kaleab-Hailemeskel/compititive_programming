# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
def is_prime(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
        
        
        
def sol():	
    
    num = int(sys.stdin.readline().strip())
    res = 0
    all_primes = []
    for n in range(2, num):
        if is_prime(n):
            all_primes.append(n)
    
    for each in range(6, num + 1):
        count_div = 0
        for prime in all_primes:
            if each % prime == 0:
                count_div += 1
        
        if count_div == 2:
            res += 1
            
                    
    
    return res
            
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())