# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
def get_min_path(graph, rail_search, last_node):
        vis = set()
        level = deque([1])
        count_level = 0
        
        while level:
            for _ in range(len(level)):
                curr_node = level.popleft()
                if curr_node == last_node:
                    return count_level
                
                for next_node in (graph[curr_node] if rail_search else range(1, last_node + 1)):
                    if (next_node in vis) or (next_node == curr_node):
                        continue
                    
                    if (rail_search) or (next_node not in graph[curr_node]): # either it has to be a rail way search or a road search i.e. shouldn't exist in the rail way route
                        vis.add(next_node)
                        level.append(next_node)
        
            count_level += 1
        
        return -1    
      
def sol():	
    n, m = map(int, sys.stdin.readline().strip().split())
    rail_graph = defaultdict(set)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        rail_graph[a].add(b)
        rail_graph[b].add(a)
    
    
    
    rail_cost = get_min_path(rail_graph, True, n)
    if rail_cost == -1:
        return -1
    
    road_cost = get_min_path(rail_graph, False, n)
    if road_cost == -1:
        return -1
    
    return max(rail_cost, road_cost)
                  
                    
                
                
                
            
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())