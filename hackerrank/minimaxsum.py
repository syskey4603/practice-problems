#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minreturn = 0
    maxreturn = 0
    for x in range(len(arr)-1):
        minreturn+=arr[x]
    for y in range(1, len(arr)):
        maxreturn +=arr[y]
    print(minreturn, maxreturn)

        
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
