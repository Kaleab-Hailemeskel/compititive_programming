# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for cost_, orig_, ch_ in zip(cost, original, changed):
            graph[orig_].append((cost_, ch_))
        
        res = 0
        from_to = [[float('inf')] * 26 for _ in range(26)]
        for col in range(26):
            from_to[col][col] = 0

        for fr, to in zip(source, target):
            heap = [(0, fr)]
            vis = set()
            fr_index, to_index = ord(fr) - ord('a'), ord(to) - ord('a')
            
            while heap and from_to[fr_index][to_index] == float('inf'):
                cost_, node_ = heappop(heap)
                if node_ in vis:
                    continue
                if node_ == to:
                    from_to[fr_index][to_index] = cost_
                    break
                vis.add(node_)
                for cost_neg, neg in graph[node_]:
                    if neg not in vis:
                        heappush(heap, (cost_neg + cost_, neg))
            
            if from_to[fr_index][to_index] == float('inf'):
                return -1
            
            res += from_to[fr_index][to_index]
        
        return res