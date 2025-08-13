# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def merge_sort(arr, split) :
    len_ = len(arr)
    if len_ < 2 or split <= 0:
        return arr, split
    split -= 1
    
    half_index = len_ // 2
    arr[half_index - 1], arr[half_index] = arr[half_index], arr[half_index - 1]
    
    left_arr = arr[:half_index]
    right_arr = arr[half_index:]
    
    res_left_arr, remaining_split = merge_sort(left_arr, split)
    res_right_arr, remaining_split = merge_sort(right_arr, remaining_split)
    
    res_left_arr.extend(res_right_arr) # merging
    
    return res_left_arr, remaining_split

    
def sol():	
    n, reverse_count = map(int, sys.stdin.readline().strip().split())
    if reverse_count % 2 == 0:
        print(-1) 
        return
    real_call = math.floor(reverse_count / 2)
    start_arr = [num for num in range(1, n + 1)]
    res, remain = merge_sort(start_arr, real_call)
    if remain <= 0:
        print(*res)
    else:
        print(-1)
    
    

itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()