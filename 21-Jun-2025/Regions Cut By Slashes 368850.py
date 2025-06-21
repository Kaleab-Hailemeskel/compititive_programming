# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class UnionFind:
    def __init__(self):
        self.parent_section = {}
    
    def find(self,node):

        if not node in self.parent_section:
            self.parent_section[node] = node
            
        parent, child = self.parent_section[node], node
        while parent != child:
            child = parent
            parent = self.parent_section[parent]
        
        self.parent_section[node] = parent
        return self.parent_section[node]
    
    def union_set(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parent_section[y] = x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        seg_union = UnionFind()
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == '\\' or grid[row][col] == ' ':
                    seg_union.union_set((row, col, 'w'), (row, col, 's'))
                    seg_union.union_set((row, col, 'n'), (row, col, 'e'))
                if grid[row][col] == '/' or grid[row][col] == ' ':
                    seg_union.union_set((row, col, 'w'), (row, col, 'n'))
                    seg_union.union_set((row, col, 'e'), (row, col, 's'))
                
                seg_union.union_set((row + 1, col, 'n'), (row, col, 's'))
                seg_union.union_set((row, col, 'e'), (row, col + 1, 'w'))
        
        seg_root = seg_union.parent_section
        return len(set(map(seg_union.find, seg_root)))
