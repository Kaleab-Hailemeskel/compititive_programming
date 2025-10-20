# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], disT: int) -> int:
        graph = defaultdict(list)
        
        for fr, to, we in edges:
            graph[fr].append((to, we))
            graph[to].append((fr, we))

        res_node = float('inf')
        res_neg_city_count = float('inf')

        for start_node in range(n):
            heap = [(0, start_node)]
            vis = set()
            while heap:
                cost, node = heappop(heap)
                if cost > disT:
                    break
                if node in vis:
                    continue
                vis.add(node)
                for next_node, next_cost in graph[node]:
                    if next_node not in vis:
                        heappush(heap, (next_cost + cost, next_node))
            
            if len(vis) - 1 <= res_neg_city_count:
                res_node = start_node
                res_neg_city_count = len(vis) - 1

        return res_node  
