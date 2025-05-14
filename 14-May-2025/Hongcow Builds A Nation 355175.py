# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque

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
class UnionFind:
    def __init__(self, size, kings):
        self.parent = {i:i for i in range(size)}
        self.size = [1] * size
        self.count_set = size
        self.number_of_edges = [0] * size
        self.king_set = kings
        
    @ bootstrap
    def find(self,node):
        if node == self.parent[node]:
            yield node
        yield_ans = yield self.find(self.parent[node])
        self.parent[node] = yield_ans
        yield self.parent[node]
    
    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y and not (x in self.king_set and y in self.king_set):
            self.count_set -= 1
            if x not in self.king_set and y in self.king_set:
                x, y = y, x
            self.size[x] += self.size[y]
            self.number_of_edges[x] += self.number_of_edges[y]
            self.parent[y] = x
        
        self.number_of_edges[x] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def get_size(self, x):
        return self.size[self.find(x)]
    
        


rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value

def sol():	
    n, m, _ = map(int, sys.stdin.readline().strip().split())
     
    set_of_kings = set(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split()))
    city = UnionFind(n, set_of_kings)
    for _ in range(m):
        fr, to = map(lambda x: int(x) - 1, sys.stdin.readline().strip().split())
        city.union_set(fr, to)
        
    largest_king = None
    largest_size = float('-inf')
    vis_city = set()
    non_king_cities = set()
    
    res_edge = 0
    
    for curr_city in range(n):
        king_of_curr_city = city.find(curr_city)
        king_city_size = city.get_size(king_of_curr_city)
        if king_of_curr_city in set_of_kings:
            if king_city_size > largest_size:
                largest_size = king_city_size
                largest_king = king_of_curr_city
        elif king_of_curr_city not in non_king_cities:
            non_king_cities.add(king_of_curr_city)

        if king_of_curr_city not in vis_city:
            
            poss_edges = (king_city_size * (king_city_size - 1)) / 2
            curr_edges = city.number_of_edges[king_of_curr_city]
            res_edge += (poss_edges - curr_edges)
        
            vis_city.add(king_of_curr_city)
    
    for curr_city in non_king_cities:
        # print(f'king_size: {city.size[largest_king]}  curr_city: {city.get_size(curr_city)}')
        res_edge += ( city.get_size(curr_city) * city.get_size(largest_king))
        city.size[largest_king] += city.get_size(curr_city)
    
    return int(res_edge)
        
            
    
            
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())