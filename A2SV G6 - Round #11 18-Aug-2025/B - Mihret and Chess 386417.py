# Problem: B - Mihret and Chess - https://codeforces.com/gym/604781/problem/B

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    r, c, fr, fc = map(int, sys.stdin.readline().strip().split())
    left_side_diagonal = lambda row, col: row + col
    right_side_diagonal = lambda row, col: row - col
    king = max(abs(fr - r), abs(fc - c))
    rook = 1 if fr == r or fc == c else 2
    bishop = 1 if left_side_diagonal(r, c) == left_side_diagonal(fr, fc) or right_side_diagonal(r, c) == right_side_diagonal(fr, fc) else 2 if ((r + c) % 2) == ((fr + fc) % 2) else 0
    return rook, bishop, king
    
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(*sol())