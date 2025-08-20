# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def inbound(two, one):
    return one[0] >= two[0] and one[1] <= two[1]

def sol():	
    n = int(input())
    prefix = Counter()
    
    bound_arr = []
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().strip().split())
        bound_arr.append((l, r, len(bound_arr) + 1))
        prefix[l] += 1
        prefix[r + 1] -= 1
    
    prefix = sorted(prefix.items())
    for i in range(1, len(prefix)):
        prefix[i] = (prefix[i][0], prefix[i][1] + prefix[i - 1][1])
    
    valid_bound = []
    
    l = 0
    for r in range(len(prefix)):
        if prefix[r][1] < 2:
            if r > l:
                left_key = prefix[l][0]
                right_key = prefix[r][0] - 1
                valid_bound.append((left_key, right_key))
            l = r + 1
    
    bound_index = 0
    valid_index = 0
    bound_arr.sort()
    
    # print(prefix)
    # print(valid_bound)
    # print(bound_arr)
    
    while valid_index < len(valid_bound) and bound_index < len(bound_arr):
        if inbound(valid_bound[valid_index], bound_arr[bound_index]):
            return bound_arr[bound_index][2]

        if valid_bound[valid_index][0] >= bound_arr[bound_index][0]:
            bound_index += 1
        else:
            valid_index += 1
            
        # print('\t',valid_index, bound_index)
    
    return -1
    
    
print(sol())