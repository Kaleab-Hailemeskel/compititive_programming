#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    n -= 1
    theNum = arr[n]
    i = n
    while i > 0 and theNum < arr[i - 1]:
        arr[i] = arr[i-1]
        printArr(arr)
        i-= 1
    arr[i] = theNum
    printArr(arr)


def printArr(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
