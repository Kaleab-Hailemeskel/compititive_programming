# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

    
def sol():	
    n, k = map(int, input().split())
    s = input()
    a = list(map(int, input().split()))
    l, r = 0, 10**9
    res = -1
    
    def check(d):
        last = 'R'
        cnt = 0
        for i in range(n):
            if a[i] > d:
                if s[i] == 'B' and last != 'B':
                    cnt += 1
                last = s[i]
        return cnt <= k
    
    while l <= r:
        m = (l + r) // 2
        if check(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    
    print(res)
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()