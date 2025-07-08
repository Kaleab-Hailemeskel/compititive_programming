# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

from collections import Counter, defaultdict

class Solution:
    def findOrder(words):
        graph = defaultdict(list)
        inlet = Counter()
        
        for each_word in words:
            for each_char in each_word:
                inlet[each_char] = 0
                
        for i in range(1, len(words)):
            the_same_but_the_first_len_greater = len(words[i-1]) > len(words[i])
            for first_char, sec_char in zip(words[i-1], words[i]):
                if first_char != sec_char:
                    the_same_but_the_first_len_greater = False
                    graph[first_char].append(sec_char)
                    inlet[sec_char] += 1
                    break
            if the_same_but_the_first_len_greater: # 
                return ""
       
        que = deque([char for char in inlet.keys() if inlet[char] == 0])
        res_order = []
        
                
        while que:
            node = que.popleft()
            res_order.append(node)
            for neg in graph[node]:
                inlet[neg] -= 1
                if inlet[neg] == 0:
                    que.append(neg)
        
        return "".join(res_order) if (not que) and len(res_order) == len(inlet) else ""
        
        # code here