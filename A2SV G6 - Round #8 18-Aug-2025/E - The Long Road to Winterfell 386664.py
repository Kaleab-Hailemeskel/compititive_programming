# Problem: E - The Long Road to Winterfell - https://codeforces.com/gym/599383/problem/E

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    k, n = map(int, sys.stdin.readline().strip().split())
    a = list(map( int, sys.stdin.readline().strip()))
    
    prefix = [ 1 - val for val in a]
    for i in range(1, k):
        prefix[i] += prefix[i - 1]
        
    def valid(m):
        for i in range(k):
            if a[i] == 0:
                left_val = prefix[i - m - 1] if i - m - 1 >= 0 else 0
                right_val = prefix[i + m] if i + m < len(prefix) else prefix[-1]
                if right_val - left_val >= n + 1:
                    return True
        return False
                 
    l, h = 1, k
    while l <= h:
        m = (l + h) // 2
        if valid(m):
            h = m - 1
        else:
            l = m + 1
    return l


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())