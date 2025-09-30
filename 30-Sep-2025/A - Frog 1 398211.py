# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

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
    arr = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(float('inf'))
    dp = [0] * (n + 1)
    for i in range(n - 2, -1, -1):
        dp[i] = min(abs(arr[i] - arr[i + 1]) + dp[i + 1], abs(arr[i] - arr[i + 2]) + dp[i + 2])
        # print(dp)
    return dp[0]
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())