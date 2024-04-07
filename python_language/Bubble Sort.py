#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    countSwap = 0
    size = len(a)
    for i in range(size):
        for j in range(size - 1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                countSwap += 1
    print(f"Array is sorted in {countSwap} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[size - 1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
