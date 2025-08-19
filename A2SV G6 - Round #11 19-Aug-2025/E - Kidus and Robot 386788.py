# Problem: E - Kidus and Robot - https://codeforces.com/gym/604781/problem/E

import sys, math
from random import randint
from bisect import bisect_left, bisect_right
from heapq import heappush, heapify, heappop
from collections import defaultdict, Counter, deque
rand_value = randint(1, 100000)
def rand(x):
    return x ^ rand_value
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def sol():	
    n_row, n_col, dis = map(int, sys.stdin.readline().strip().split())
    
    direction = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U',-1, 0)]
    opposite = {"D":"U", "U":"D", "L":"R", "R":"L"}
    
    grid = []
    for _ in range(n_row):
        grid.append(list(map(str, sys.stdin.readline().strip())))
    
    if dis % 2 == 1:
        return "IMPOSSIBLE"
    
    in_bound = lambda x, y: 0 <= x < n_row and 0 <= y < n_col
    row = col = float('inf')
    
    for i in range(n_row):
        for j in range(n_col):
            if grid[i][j] == 'X':
                row = i
                col = j
                break
        if row != float('inf'):
            break
    origin = (row, col)
    # going forward
    stack = []
    for i in range(dis // 2):
        for char, dx, dy in direction:
            nx, ny = row + dx, col + dy
            if in_bound(nx, ny) and grid[nx][ny] != '*':
                stack.append(char)
                row, col = nx, ny
                break
    min_dis_from_start = [[0] * n_col for _ in range(n_row)]
    # populate the distance from the start
    que = deque([origin])
    while que:
        for _ in range(len(que)):
            curr_row, curr_col = que.popleft()
            for _, dx, dy in direction:
                nx, ny = curr_row + dx, curr_col + dy
                if in_bound(nx, ny) and grid[nx][ny] != '*' and min_dis_from_start[nx][ny] == 0 and (nx, ny) != origin:
                    min_dis_from_start[nx][ny]  = min_dis_from_start[curr_row][curr_col] + 1
                    que.append((nx, ny))

    # for val in min_dis_from_start:
    #     print(val)
    # returning back
    returning_back = dis // 2
    calc_dis = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
    que = deque([(row, col)])     
    while que:
        # print(que)
        for _ in range(len(que)):
            curr_row, curr_col = que.popleft()
            for char, dx, dy in direction:
                nx, ny = curr_row + dx, curr_col + dy
                if in_bound(nx, ny) and grid[nx][ny] != '*' and min_dis_from_start[nx][ny] <= returning_back:
                    que.append((nx, ny))
                    stack.append(char)
                    break
        returning_back -= 1
      
    if stack:
        return ''.join(stack)
    
    return "IMPOSSIBLE"
                    
        
        
    
        
                
                   
    for i in range(len(stack) - 1, -1, -1):
        stack.append(opposite[stack[i]])
  

    
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())