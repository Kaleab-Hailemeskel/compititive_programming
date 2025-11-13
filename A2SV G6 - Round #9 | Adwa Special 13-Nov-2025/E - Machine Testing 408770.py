# Problem: E - Machine Testing - https://codeforces.com/gym/601269/problem/E

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
    h = list(map(int, sys.stdin.readline().strip().split()))
    p = list(map(int, sys.stdin.readline().strip().split()))
    remained_guns = [(p[0], float('inf'))]
    max_res = float('-inf')
    for i in range(1, n):        
        time_to_die = 0
        while (remained_guns[-1][0] * remained_guns[-1][1]) <= h[i]:
            last_gun_power, last_gun_remain_time = remained_guns.pop()
            time_to_die += last_gun_remain_time
            h[i] -= (last_gun_power * last_gun_remain_time)

        
        last_gun_power, last_gun_remain_time = remained_guns.pop()        
        last_gun_remain_time -= math.ceil(h[i] / last_gun_power)
        remained_guns.append((last_gun_power, last_gun_remain_time))
            
        remain_time_from_the_last_gun_injury = math.ceil(h[i] / remained_guns[-1][0])
        tot_remain = time_to_die + remain_time_from_the_last_gun_injury

        max_res = max(
            max_res, 
            tot_remain
        )
                
        remained_guns.append((p[i], tot_remain))
    
    return max_res if max_res != float('-inf') else 0
    
            
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())
    # print('\n')