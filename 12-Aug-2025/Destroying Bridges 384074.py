# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

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
    if k >= (n - 1):
        print(1)
    else:
        print(n)
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()