# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

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
    mid_bisections = Counter()
    points = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())                
        points.append((x, y))
    
    for i in range(n - 1):
        x, y = points[i]
        for j in range(i + 1, n):
            old_x, old_y = points[j]
            mid_x = x + old_x
            mid_y = y + old_y
            
            mid_bisections[(mid_x, mid_y)] += 1
            

    
    return sum(math.comb(count, 2) for count in mid_bisections.values())
        
        
    
    
                
                
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())