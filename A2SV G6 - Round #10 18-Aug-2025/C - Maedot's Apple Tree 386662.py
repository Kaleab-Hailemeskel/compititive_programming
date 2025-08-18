# Problem: C - Maedot's Apple Tree - https://codeforces.com/gym/602812/problem/C

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def sol():	
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)
    child_value = defaultdict(int)
    @bootstrap
    def dfs(node, parent):
        has_child = False
        res = 0
        for child in graph[node]:
            if child != parent:
                value = yield dfs(child, node)
                res += value
                child_value[child] = value
                has_child = True
        if has_child:
            yield res
        yield 1
    child_value[1] = dfs(1, 1)
    for _ in range(int(sys.stdin.readline().strip())):
        a, b = map(int, sys.stdin.readline().strip().split())
        print(child_value[a] * child_value[b])
        
    
                
                
        
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()