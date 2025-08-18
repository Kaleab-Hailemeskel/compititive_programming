# Problem: D - Merbebt and Maze - https://codeforces.com/gym/604781/problem/D

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
    f = list(map(int, sys.stdin.readline().strip().split()))
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)
        
    level = deque((val, val) for val in f)
    level.append((1, 1))
    
    vis = set(f)
    vis.add(1)
   
    first_vis = [-1 for _ in range(n + 1)]
 
    curr_level = 0
    while level:
        curr_level += 1
        for _ in range(len(level)):
            node, ansc = level.popleft()
            
            for neg_node in graph[node]:
                if neg_node not in vis:
                    vis.add(neg_node)
                    level.append((neg_node, ansc))
                    
                    if len(graph[neg_node]) == 1:
                        first_vis[neg_node] = ansc
                        
    # print(first_vis)
    for val in first_vis:
        if val == 1:
            return "YES"
    return "NO"

    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    (sys.stdin.readline().strip())
    print(sol())