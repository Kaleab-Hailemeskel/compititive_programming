# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

import sys
def sol():	
    n, m = map(int, sys.stdin.readline().strip().split())

    strs = sys.stdin.readline().strip()
    graph = [[] for _ in range(n)]
    in_count = [0] * n
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        in_count[b] += 1
    
    stack = []
    for node in range(n):
        if in_count[node] == 0:
            stack.append(node)    

    res = float('-inf')
    cc = [([0] * n) for _ in range(26)]
    node_count = 0
    while stack:
        node = stack.pop()
        node_count += 1
        char_index = ord(strs[node]) - ord('a')
        cc[char_index][node] += 1
        
        res = max(res, cc[char_index][node])
        for neg in graph[node]:
            for k in range(26):
                cc[k][neg] = max(cc[k][neg], cc[k][node])
                
            in_count[neg] -= 1
            if in_count[neg] == 0:
                stack.append(neg)
            

    return res if node_count == n else -1

itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())