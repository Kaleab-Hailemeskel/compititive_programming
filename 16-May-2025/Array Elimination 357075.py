# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

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
    a = list(map(int, sys.stdin.readline().strip().split()))
    cnt = [0] * 32
    for bit in range(32):
        for num in a:
            cnt[bit] += bool(num & (1 << bit))  
    
    divisors = [0] * (n + 1)
    for num in cnt:
        for i in range(1,n + 1):
            if num % i == 0:
                divisors[i] += 1
    ans = []
    for divisor in range(1, len(divisors)):
        if divisors[divisor] == 32:
            ans.append(divisor)
    return ans
              
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(*sol())