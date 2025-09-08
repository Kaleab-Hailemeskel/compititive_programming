# Problem: E - Cycle in Graph - https://codeforces.com/gym/602812/problem/E

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
last_index_map = defaultdict(int)
def sol():	
    n, m, dis = map(int, sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)
    vis = defaultdict(int)
    res = []
    start_node = []
    the_two_node = []
    @bootstrap
    def dfs(node, level):
        nonlocal dis
        vis[node] = level
        
        for neg in graph[node]:
            if neg in vis:
                if abs(level - vis[neg]) >= dis:
                    len_ = abs(level - vis[neg])
                    start_node.append(neg)
                    the_two_node.extend([neg, node, len_])
                    yield True
            else:
                last_index_map[neg] = len(res)
                res.append(neg)
                ret = yield dfs(neg, level + 1)
                if ret:
                    yield True
                res.pop()
        
        del vis[node]
        
        yield False
    for node in range(1, n + 1):
        if node not in vis:
            res.append(node)
            ret = dfs(node, 0)
            if ret:
                break
    ans_res = res[last_index_map[start_node.pop()]:]
    print(len(ans_res))     
    return ans_res
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(*sol())