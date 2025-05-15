# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

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
    graph = defaultdict(list)
    just_node = None
    
    for _ in range(n - 1):
        fr, to = map(int, sys.stdin.readline().strip().split())
        just_node = to
        graph[fr].append(to)
        graph[to].append(fr)
     

    def bfs(node):
        order = deque([(node, node)])
        farthest_node = node
        step = -1
        while order:
            for _ in range(len(order)):
                curr, prev = order.popleft()
                has_child = False
                for neg in graph[curr]:
                    if neg != prev:
                        has_child = True
                        order.append((neg, curr))
                if not has_child:
                    farthest_node = curr
            step += 1
        
        return farthest_node, step
    
    farthest_node, _ = bfs(just_node)
    farthest_node, max_rad = bfs(farthest_node)
    
    
    
    
            
        
    return max_rad * 3
    
    
                
        
            
    

    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())