# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    n, m = map(int, sys.stdin.readline().strip().split())
    c = Counter()
    c[2] += n // 2
    c[1] += n % 2
    while c[2] >= 0 and (c[2] + c[1]) % m != 0:
        c[2] -= 1
        c[1] += 2
    
    return c[2] + c[1] if c[2] >= 0 else -1
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())