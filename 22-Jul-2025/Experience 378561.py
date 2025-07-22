# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
        self.parent = {i:i for i in range(size)}
        self.rank = [1] * size
        self.power = [0] * size
        self.count_set = size
    
    def find(self,node):
        tot_sum = 0
        while node != self.parent[node]:
            tot_sum += self.power[node]
            node = self.parent[node]
        return (node, tot_sum + self.power[node])
    
    def add(self, node,  power_ranger):
        parent, _ = self.find(node)
        # print(f'adding @: {power_ranger}  parent: {parent}')
        self.power[parent] += power_ranger
            
    def union_set(self, x, y):
        x, _ = self.find(x)
        y, _ = self.find(y)
        if x != y:
            self.count_set -= 1
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            elif self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.parent[y] = x
            # print(f'y: {y}\ty_power: {self.power[y]}')
            # print(f'x: {x}\tx_power: {self.power[x]}')
            self.power[y] -= self.power[x]
            
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
def sol():	
    n, m = map(int, sys.stdin.readline().strip().split())
    uni = UnionFind(n)
    for _ in range(m):
        a = list(map(str, sys.stdin.readline().strip().split()))
        if a[0] == 'add':
            uni.add(int(a[1]) - 1, int(a[2]))
        elif a[0] == 'join':
            uni.union_set(int(a[1]) - 1, int(a[2]) - 1)
        else:
            print(uni.find(int(a[1]) - 1)[1])
            
    
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    sol()