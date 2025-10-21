# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
def factorize(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    return num
def sol():
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    init = factorize(arr[0])
    return 'Yes' if all( factorize(num) == init for num in arr) else 'No'
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())