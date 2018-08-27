#!/bin/python

import math
import os
import random
import re
import sys
from bisect import *

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    rl,rank,scores[0] = [1],1,-scores[0]
    for i in range(1,len(scores)):
        scores[i] = -scores[i]
        if scores[i] == scores[i-1]:
            rl.append(rank)
        else:
            rank +=1
            rl.append(rank)
    print scores, rl
    res = []
    for v in alice: 
        i = -v
        idx = bisect_left(scores, i)
        if idx == len(scores): 
            res.append(rl[-1] + 1)
        elif idx == 0:
            res.append(1)
        else:
            res.append(rl[idx])
                
    print res
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    scores_count = int(raw_input())
    scores = map(int, raw_input().rstrip().split())
    alice_count = int(raw_input())
    alice = map(int, raw_input().rstrip().split())
    print scores, alice
    result = climbingLeaderboard(scores, alice)
    print result
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

