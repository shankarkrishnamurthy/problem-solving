
#!/bin/python

import math
import os
import random
import re
import sys

# 
# Complete the timeInWords function below.
def timeInWords(h, m):
    mw = ["o' clock", 'one minute', 'two minutes','three minutes', 'four minutes', 'five minutes', 'six minutes', 'seven minutes', 'eight minutes', 'nine minutes', 'ten minutes', 'eleven minutes', 'twelve minutes', 'thirteen minutes', 'fourteen minutes', 'quarter', 'sixteen minutes', 'seventeen minutes','eighteen minutes','sixteen minutes', 'twenty minutes', 'twenty one minutes', 'twenty two minutes', 'twenty three minutes', 'twenty four minutes',  'twenty five minutes', 'twenty six minutes', 'twenty seven minutes', 'twenty eight minutes',  'twenty nine minutes', 'half' ]
    hw = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    if m == 0:
        tiw = hw[h] + ' ' + mw[m]
    elif m > 30:
        tm = 60 - m
        h = (h + 1) % 13
        tiw = mw[tm] + ' to ' + hw[h]
    else:
        tiw = mw[m] + ' past ' + hw[h]
    return tiw

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(raw_input())

    m = int(raw_input())

    result = timeInWords(h, m)
    print result

    fptr.write(result + '\n')

    fptr.close()
