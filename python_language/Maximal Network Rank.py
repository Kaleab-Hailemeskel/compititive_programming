class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        conn = defaultdict(set)
        di = {}
        for f, t in roads:
            conn[f].add(t)
            conn[t].add(f)
        
        max_conn = 0
        for f in range(n):
            for t in range(f+1, n):
                max_conn = max(max_conn, len(conn[f]) + len(conn[t]) - (f in conn[t]))
        return max_conn
        
        
            
        
