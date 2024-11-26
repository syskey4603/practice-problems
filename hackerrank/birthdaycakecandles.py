#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candles.sort(reverse=True)
    maxval = candles[0]
    temp = 0
    returnval = 0
    curval = candles[temp]
    while curval == maxval:
        if temp == len(candles)-1:
            return len(candles)
        returnval+=1
        temp+=1
        curval = candles[temp]
    return(returnval)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
