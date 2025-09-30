# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

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
    n = int(sys.stdin.readline().strip())
    days = []
    for _ in range(n):
        days.append(tuple(list(map(int, sys.stdin.readline().strip().split()))))
    dp = {}
    def opp(num):
        if num == 1:
            return 0, 2
        if num == 2:
            return 0, 1
        return 1, 2
    @bootstrap
    def recur(day_index, choice):
        if day_index == len(days):
            yield 0
        if (day_index, choice) not in dp:
            other_one, other_two = opp(choice)
            one = yield recur(day_index + 1, other_one)
            two = yield recur(day_index + 1, other_two)
            dp[(day_index, choice)] = days[day_index][choice] + max(one, two)
        yield dp[(day_index, choice)]
    
    return max(recur(0, choice) for choice in (0, 1, 2))
        
    pass # Remove
    


itt = 1
# itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())