# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_taken = [-float('inf')] * (n)
        graph = defaultdict(list)

        for fr, to, time in times:
            graph[fr].append((to, time))
        
        heap = [(0, k)]
        
        while heap:
            curr_time, curr_node = heappop(heap)
            if time_taken[curr_node - 1] != -float('inf'):
                continue
            
            time_taken[curr_node - 1] = curr_time
            
            for neg, cost_time in graph[curr_node]:
                tot_time_needed = cost_time + curr_time
                if time_taken[neg - 1] == -float('inf'):
                    heappush(heap, (tot_time_needed, neg))
        
        res, res_min = max(time_taken),min(time_taken)
        
        return -1 if res_min == -float('inf') else res # i.e. if there exist a node that wasn't accessed from the k node



