# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

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
    a = list(map(str, sys.stdin.readline().strip()))
    clock_wise, both_dir, counter_clock_wise = ">", "-", "<"
    
    # clockwise
    collect_set = set()
    res_set = set()
    for i in range(2 * n + 1):
        curr_belt, prev_belt = (i % n), ((i - 1) % n)
        if a[curr_belt] == counter_clock_wise:    
            collect_set = set()
            
        
        if both_dir not in (a[curr_belt], a[prev_belt]):    
            if curr_belt in collect_set:        
                collect_set.remove(curr_belt)
                res_set.add(curr_belt)
            elif a[curr_belt] == clock_wise:        
                collect_set.add(curr_belt)
            else:        
                collect_set = set()
        else:    
            res_set.add(curr_belt)
            
    # anti-clockwise
    counter_collect_set = set()
    counter_res_set = set()
    for i in range(-1, -2 * n - 1, -1):
        curr_belt, next_belt = (i % n), ((i + 1) % n)
        if a[curr_belt] == clock_wise:    
            counter_collect_set = set()
            
        if both_dir not in (a[curr_belt], a[next_belt]):    
            if curr_belt in counter_collect_set:        
                counter_collect_set.remove(curr_belt)
                counter_res_set.add(curr_belt)
            elif a[curr_belt] == counter_clock_wise:        
                counter_collect_set.add(curr_belt)
            else:        
                counter_collect_set = set()
        else:    
            counter_res_set.add(curr_belt)
        
    print(max(len(res_set), len(counter_res_set))) 
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()