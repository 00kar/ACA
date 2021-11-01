#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    b = list(b)
    count = 0
    for i in range(n-2):
        if b[i] == '0' and b[i+1] == '1' and b[i+2] == '0':
            count += 1
            b[i+2] = '1'
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()

