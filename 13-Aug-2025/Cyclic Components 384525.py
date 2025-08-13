# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

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
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)
    vis = set()
    res = 0
    for node in range(1, n + 1):
        if node not in vis:
            curr_graph_contain_cycle = True
            stack = [node]
            vis.add(node)
            
            while stack:
                curr_node = stack.pop()
                if len(graph[curr_node]) != 2:
                    curr_graph_contain_cycle = False
                for neg_node in graph[curr_node]:
                    if  neg_node not in vis:
                        vis.add(neg_node)
                        stack.append(neg_node)
                        
            if curr_graph_contain_cycle:
                res += 1
                    
    print(res)    
                
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()