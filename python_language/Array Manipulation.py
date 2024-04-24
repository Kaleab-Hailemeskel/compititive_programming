#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    
    
    arr = [0] * (n + 1)
    for index in range(len(queries)):
        left, right, value = queries[index][0], queries[index][1], queries[index][2]
        arr[left - 1] += value
        arr[right] -= value
    
    hold = 0
    max_value = 0
    for index in range(n + 1):
        hold += arr[index]
        arr[index] = hold
        max_value = max(max_value, hold)
    
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
