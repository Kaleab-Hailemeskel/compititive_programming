# Problem: D - The Road to King's Landing - https://codeforces.com/gym/599383/problem/D

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
def have_int(curr, prev):
    return (max(curr[0], prev[0]) <= min(curr[1], prev[1]))
def get_int(curr, prev):
    return [max(curr[0], prev[0]), min(curr[1], prev[1])]
    
def sol():	
    n = int(sys.stdin.readline().strip())
    arr = []
    for _ in range(n):
        arr.append(tuple(map(int, sys.stdin.readline().strip().split())))
    
    def valid(m):
        curr_range = [0,0]
        for prev in arr:
            curr_range[0] -= m
            curr_range[1] += m
            if have_int(curr_range, prev):
                curr_range = get_int(curr_range, prev)
            else:
                return False
        return True
    
        
                
    l, h = 0, int(10e9)
    while l <= h:
        m = (l + h) // 2
        if valid(m):
            h = m - 1
        else:
            l = m + 1
    return l
        
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())