# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F

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
    return sum( math.comb(n, m) for m in range(5, 8))
    
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())