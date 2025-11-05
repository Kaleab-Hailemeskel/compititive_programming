# Problem: Second Minimum Time to Reach Destination - https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        curr_time = 0
        short_dis = [float('inf')] * (n + 1)
        short_2nd = [float('inf')] * (n + 1)
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        heap = [(0, 1)]
        
        while heap:
            dis, node = heappop(heap)
            if short_dis[node] != float('inf') and (short_dis[node] < dis < short_2nd[node] ):
                short_2nd[node] = dis
            elif short_dis[node] == float('inf'):
                short_dis[node] = dis    
            else:
                continue
            
            for neg in graph[node]:
                if short_2nd[neg] == float('inf'):
                    heappush(heap, (dis + 1, neg))
       
        min_2nd = short_2nd[n]
        curr_time = 0
        STOPPING_PHASE = 1
        # calculation for the trafic signal delay
        for step in range(min_2nd):
            curr_time += time
            if (curr_time // change) % 2 == STOPPING_PHASE and step != min_2nd - 1:
                remain_time = change - (curr_time % change)
                curr_time += remain_time
        return curr_time


        