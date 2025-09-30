# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    n, k = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    for _ in range(k - 1):
        arr.append(float('inf'))
    dp = [0] * (n + k - 1)
    for i in range(n - 2, -1, -1):
        curr_min = float('inf')
        for add in range(1, k + 1):
            curr_min = min(curr_min, abs(arr[i] - arr[i + add]) + dp[i + add])
        dp[i] = curr_min
        # print(dp)
    return dp[0]
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())
    