# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    n, m = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    start_node = 1
    initial_cost = 0
    heap = [(initial_cost, start_node, start_node)]
    vis = set()
    child_parent = {}
    while heap:
        curr_cost, curr_node, parent_node = heappop(heap)
        if curr_node in vis:
            continue
        
        child_parent[curr_node] = parent_node
        vis.add(curr_node)
        
        if curr_node == n:
            break
        for next_node, next_cost in graph[curr_node]:
            if next_node not in vis:
                heappush(heap, (next_cost + curr_cost, next_node, curr_node))
    
    if n not in vis:
        return [-1]
    res = [n]
    node = n
    while True:
        res.append(child_parent[node])
        node = child_parent[node]
        if node == child_parent[node]:
            break
    res.reverse()
    return res 
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(*sol())