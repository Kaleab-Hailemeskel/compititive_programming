# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.rank = [1] * size
        self.count_set = size
    
    def find(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.count_set -= 1
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            elif self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.parent[y] = x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edge_heap = []
        q_heap = []
        res = [False] * len(queries)
        for fr, to, path_len in edgeList:
            heappush(edge_heap, (path_len, fr, to))
        
        for index, (fr, to, path_len) in enumerate(queries):
            heappush(q_heap, (path_len, fr, to, index))

        uni = UnionFind(n)

        while q_heap:
            q_len, q_fr, q_to, q_index = heappop(q_heap)
            while edge_heap and edge_heap[0][0] < q_len:
                edge_path, edge_fr, edge_to = heappop(edge_heap)
                uni.union_set(edge_fr, edge_to)
            
            res[q_index] = uni.connected(q_fr, q_to)
        
        return res
        

        