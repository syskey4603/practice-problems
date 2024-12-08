#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    poslen = 0
    zerolen = 0
    neglen = 0
    
    for x in arr:
        if x > 0:
            poslen +=1
        elif x == 0:
            zerolen +=1
        elif x < 0:
            neglen +=1
        
    posfinal = poslen/len(arr)
    negfinal = neglen/len(arr)
    zerofinal = zerolen/len(arr)
        
    print(posfinal)
    print(negfinal)
    print(zerofinal)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
