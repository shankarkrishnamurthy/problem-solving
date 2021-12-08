#!/bin/python
import os,sys
import re
import math,random

def maxEvents(arrival, duration):
    ev = []
    for i,v in enumerate(arrival):
        ev.append((v,'S',i))
        ev.append((duration[i]+v,'E',i))
    ev.sort()
    max_ev_sofar,st=0,[0]*len(arrival)
    for t,e,i in ev:
        #print(t,e,i)
        if e=='S':
            st[i] = max_ev_sofar
        else: # e=='E'
            max_ev_sofar = max(max_ev_sofar, st[i]+1)

    return max_ev_sofar 
        
print(maxEvents([1, 3, 3, 5, 7],[2, 2, 1, 2, 1]))
print(maxEvents([1, 3, 5],[2, 2, 2]))
        
