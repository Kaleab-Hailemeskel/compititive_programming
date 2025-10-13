# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    count_factors = Counter()
    def add_factor(num):
        factor = 2
        while factor * factor <= num:
            while num % factor == 0:
                count_factors[factor] += 1
                num //= factor
            factor += 1
        if num > 1:
            count_factors[num] += 1
    for num in arr:
        add_factor(num)
    
    for times in count_factors.values():
        if times % n != 0:
            return 'NO'
    
    return "YES"
    
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())