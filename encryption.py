#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the encryption function below.
def encryption(s):
    length = len(s)
    l = math.sqrt(length)

    f = math.floor(l)
    # print(f)
    c = math.ceil(l)
    # print(c)
    rc = f * c
    rc1 = c * c

    rc2 = min(rc, rc1)
    # print(rc2)
    if rc2 < length:
        f = c
    # print(f)
    # if rc2 >=length:

    str = ""

    for col in range(c):

        for row in range(f):

            if (c * row + col) < length:
                str = str + s[c * row + col]

        str = str + " "

    return str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
