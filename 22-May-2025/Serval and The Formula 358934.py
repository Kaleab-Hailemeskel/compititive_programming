# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == b:
        print(-1)
        return
    if a < b:
        a, b = b, a
        
    power = 0
    while 1 << power < a:
        power += 1
    k = (1 << power) - a
    print(k)
    # print((a + k) + (b + k), (a + k) ^ (b + k))
    
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()