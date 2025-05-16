# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

import sys

def sol():	
    n = int(sys.stdin.readline().strip())
    res = 0
    first_set_bit = -1
    for i in range(31):
        if n & (1 << i):
            res |= (1 << i)
            first_set_bit = i
            break
                
    if res != n:
        return res

    if first_set_bit == 0:
    
        return res | (1 << (first_set_bit + 1))
    
    return res | 1
    
    


itt = 1
itt = int(int(sys.stdin.readline().strip()))
for _ in range(itt):
    print(sol())