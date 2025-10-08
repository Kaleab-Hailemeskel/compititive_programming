# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

import sys
from random import randint
# sys.setrecursionlimit(10**7)
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
   
    memo = [[0]+[float('inf')] * 100000 for _ in range(size + 1)]
    
    
    
   
    for index in range(size):
        for value in range(100000+1):
            remain_value = value - values[index]
            memo[index][value] = memo[index-1][value]
            if remain_value >= 0:
                memo[index][value] = min(
                    memo[index-1][value],
                    weights[index] + memo[index-1][remain_value]
                )
    res = float('-inf')
    for i in range(len(memo[0]) - 1, -1, -1):
        val = memo[size-1][i]
        if val <= weight_capacity:
            res = max(res, i)
    return res
            
        
   
        
        
        
       
    
    
    
    
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())