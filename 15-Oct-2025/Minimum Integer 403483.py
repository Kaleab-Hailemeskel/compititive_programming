# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    l, r, k = map(int, sys.stdin.readline().strip().split())
    if k < l or k > r:
        return k
    return (math.floor(r / k) + 1) * k
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())