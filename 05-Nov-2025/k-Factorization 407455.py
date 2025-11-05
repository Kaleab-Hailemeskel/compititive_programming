# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    n, k = map(int, sys.stdin.readline().strip().split())
    def factors(num):
        div = 2
        factor_count = set()
        while num >= div:
            while num % div == 0:
                factor_count.add(div)
                num //= div
            div += 1
        if num != 1:
            factor_count.add(num)
        return factor_count
    res = []
    facts = factors(n)
    for fact in facts:
        while n % fact == 0 and len(res) < k:
           res.append(fact)
           n //= fact
        if len(res) == k:
            break
        
    res[-1] *= n
    if len(res) != k:
        print(-1)
    else:
        print(*res)
        
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()