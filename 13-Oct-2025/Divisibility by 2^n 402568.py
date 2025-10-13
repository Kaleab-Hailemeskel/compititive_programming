# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

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
    wanted_2th_pow = n
    arr = list(map(int, sys.stdin.readline().strip().split()))
    def give_power_of_two(num):
        pow = 0
        while num % 2 == 0:
            num //= 2
            pow += 1
        return pow
    
    factor_two = []
    two_count = 0
    
    for index, num in enumerate(arr):
        # print(f'\t{give_power_of_two(num)}')
        two_count += give_power_of_two(num)
        factor_two.append(give_power_of_two(index + 1))
       
    # print(f'{two_count = } {wanted_2th_pow = }')
    if wanted_2th_pow <= two_count:
        return 0
    
    factor_two.sort(reverse=True)
    for index, each_pow in enumerate(factor_two):
        two_count += each_pow
        if wanted_2th_pow <= two_count:
            return index + 1
    return -1
        
        


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())
    
    