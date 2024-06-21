from collections import defaultdict
def return_1():
    return []
n, m = map(int, input().split())

groupA = defaultdict(return_1)
for i in range(n):
    groupA[input()].append(i+1)

for i in range(m):
    char = input()
    print(*groupA[char]) if len(groupA[char]) > 0 else print(-1)

    
    
