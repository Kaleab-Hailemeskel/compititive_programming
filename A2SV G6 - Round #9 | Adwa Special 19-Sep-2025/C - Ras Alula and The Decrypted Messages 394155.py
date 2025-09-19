# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

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
    main = sys.stdin.readline().strip()
    key = sys.stdin.readline().strip()
    prefix_main = [0]
    tot_key = sum(map(lambda a : ord(a) - ord('a') + 1, key))
    for val in map(ord, main):
        prefix_main.append(prefix_main[-1] + (val - ord('a') + 1))
    
    for r in range(m, len(prefix_main)):
        l = r - m
        if prefix_main[r] - prefix_main[l] == tot_key:
            return "YES"
    return "NO"
    
    print(prefix_main)
    print(tot_key)
        
    
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())