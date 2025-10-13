# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

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
    a = list(map(int, sys.stdin.readline().strip().split()))
    b = list(map(int, sys.stdin.readline().strip().split()))
    
    a = sorted(list(set(a)))
    other = [val - a[0] for val in a[1:]]
    
    if other:
        gcd = math.gcd(*other)
        res = []    
        for num in b:
            res.append(math.gcd(num + a[0], gcd))
        return res
    else:
        return [a[0] + num for num in b]
        
        
    
    
        
        
    
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(*sol())