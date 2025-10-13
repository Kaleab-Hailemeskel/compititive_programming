# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    a, b = list(map(str, sys.stdin.readline().strip().split()))
    if a == b:
        return a
    return 1
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())