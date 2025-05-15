# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
class UnionFind:
    def __init__(self, size, original):
        self.parent = {i:i for i in range(size)}
        self.size = [1] * size
        self.count_set = size
        self.root_set = defaultdict(Counter)
        for index, char in enumerate(original):
            self.root_set[index][char] += 1
    
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union_set(self,x, y, x_val, y_val ):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.count_set -= 1
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.size[x] += self.size[y]
            self.root_set[x].update(self.root_set[y])
            self.parent[y] = x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def get_delete(self, char, index):
        root = self.find(index)
        if char in self.root_set[root]:
            self.root_set[root][char] -= 1
            if self.root_set[root][char] == 0:
                del self.root_set[root][char]
            return True
        return False
    
def sol():	
    n, m = map(int, sys.stdin.readline().strip().split())
    orginal = sys.stdin.readline().strip()
    swapped = sys.stdin.readline().strip()
    
    uni = UnionFind(n, orginal)
    for i in range(n):
        if i + m < n:
            uni.union_set(i, i + m, orginal[i], orginal[i + m])
        if i + m + 1 < n:
            uni.union_set(i, i + m + 1, orginal[i], orginal[i + 1 + m])
    
    
    
    return 'YES' if all (uni.get_delete(value, index) for index, value in enumerate(swapped)) else 'NO'



itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())