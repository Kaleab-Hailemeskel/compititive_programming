# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        node_prob = [0] * n
        for i in range(len(succProb)):
            edge = edges[i]
            prob = succProb[i]
            graph[edge[0]].append([edge[1], prob])
            graph[edge[1]].append([edge[0], prob])
        
        heap = []
        heappush(heap, (-1, start_node))
        while heap:
            prob, num = heappop(heap)
            if num == end_node:
                return -prob
            if node_prob[num] != 0:
                continue

            node_prob[num] = -prob
            for adj, adj_prob in graph[num]:
                if node_prob[adj] == 0:
                    heappush(heap, (adj_prob * prob, adj))
        
        
        return 0