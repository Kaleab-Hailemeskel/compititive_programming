class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        start = set(edge[0] for edge in edges)
        destination = set(edge[1] for edge in edges)
        
        ans = []
        for ele in start:
            if ele not in destination:
                ans.append(ele)
        return ans
