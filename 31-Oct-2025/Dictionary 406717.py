# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    s = sys.stdin.readline().strip()
    num_a, num_b = map(lambda a: ord(a) - ord('a'), s)
    # print(f'{num_a, num_b}')
    return (num_a * 26 + (num_b + 1)) - ((num_a + 1) if num_a < num_b else (num_a))
    
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())