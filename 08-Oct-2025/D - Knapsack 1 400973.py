# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
sys.setrecursionlimit(10**7)
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():  
    size, weight_capacity = map(int, sys.stdin.readline().strip().split())

    weights = []
    values = []
    for _ in range(size):
        w, v = map(int, sys.stdin.readline().strip().split())
        weights.append(w)
        values.append(v)
    
    memo = [0] + [float('-inf')] * (weight_capacity)
    memo2 = list(memo)
    
    # The size + 1 for the memoization table is clever because the last row will remain initialized to float('-inf') 
    # throughout every iteration of the next loop. This effectively keeps the size+1 row as a reference to the 
    # initial "no answer found" state.
    
    for index, curr_weight in enumerate(weights):
        for wanted_weight in range(1, weight_capacity + 1):
            remain_weight = wanted_weight - curr_weight
            memo[wanted_weight] = memo2[wanted_weight]
            if remain_weight >= 0:
                # Comparing the maximum value achievable without the current item (memo[index][wanted_weight])
                # to the maximum value achievable by taking the current item (values[index] + memo[index - 1][remain_weight]).
                
                memo[wanted_weight] = max(
                    memo[wanted_weight],
                    values[index] + memo2[remain_weight]
                )
        memo2 = list(memo)
        
    # Since the last row of the memoization table (memo[size]) is used only for initialization purposes 
    # and not for storing results, the final answer is found in the second-to-last row (memo[-2] or memo[size-1]).
    
    return max(memo)
            


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())