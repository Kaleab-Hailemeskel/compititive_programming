# Problem: E - Simple Cycle With Minimal Lightest Edge - https://codeforces.com/gym/607625/problem/E

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(1, size + 1)}
        self.min_weight = {i : float('inf') for i in range(1, 1 + size)}
        self.rank = [1] * (size + 1)
        self.count_set = size
    
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union_set(self, x, y, weight):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.count_set -= 1
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            elif self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.min_weight[x] = min(self.min_weight[x], self.min_weight[y], weight)
            self.parent[y] = x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
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
    heap = []
    graph = defaultdict(list)
    min_size, a, b, = float('inf'), float('inf'), float('inf')
    
    size, edge = map(int, sys.stdin.readline().strip().split())
    un = UnionFind(size)
    for _ in range(edge):
        aa, bb, w = map(int, sys.stdin.readline().strip().split())
        heappush(heap, (-w, aa, bb))
        heappush(graph[aa], (w, bb))
        heappush(graph[bb], (w, aa))
        if min_size > w:
            min_size = w
            a = aa
            b = bb
    # knowing the start and end node
    last_ans = []
    while heap:
        w, a, b = heappop(heap)
        if un.connected(a, b):     
            last_ans = [a, b, -w]
        un.union_set(a, b, w)
    
    # print(f'from {a}  to {b}')
    # knowing the min weight of edge found between them
    level = defaultdict(lambda : float('-inf'))
    a, b, w = last_ans
    expected = a
    res_path = [b]
    
    @bootstrap
    def dfs(node, parent):    
        nonlocal expected
            
        min_res = (float('inf'), float('inf'))
        for neg_weight, neg_node in graph[node]:
            if neg_node == parent:
                continue
            
            if neg_node == expected:
                res_path.append(neg_node)
                yield True
            if neg_node in level:
                continue
            
            level[neg_node] = level[node] + 1
            res_path.append(neg_node)
            res = yield dfs(neg_node, node)
            if res:
                yield True
            res_path.pop()
        yield False
    
    level[b] = 0
    res = dfs(b, a)
    
    print(w, len(res_path))
    return res_path
    return 
        
            
    
        
    
    
    pass # Remove
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(*sol())