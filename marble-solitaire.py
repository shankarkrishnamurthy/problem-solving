import numpy as np
from copy import deepcopy as dc
import time

class Solution(object):
    def __init__(self):
        self.alld=set()
        self.occu = dict()

    def do_solve(self, occu, anc):

        def is_up(i,j):
            return (i-1,j) in occu and (i-2,j) in occu
        def is_down(i,j):
            return (i+1,j) in occu and (i+2,j) in occu
        def is_left(i,j):
            return (i,j-1) in occu and (i,j-2) in occu
        def is_right(i,j):
            return (i,j+1) in occu and (i,j+2) in occu

        if len(occu) not in self.occu:
            self.occu[len(occu)] = 1
            print "Reached occu = ", len(occu)
            print anc
            
        if len(occu) == 1:
            print "Hurray! Success"
            print anc
            return

        free= self.alld-occu
        for (i,j) in free:
            if is_up(i,j): 
                occucp = dc(occu)
                occucp.remove((i-1,j))
                occucp.remove((i-2,j))
                occucp.add((i,j))
                self.do_solve(occucp, anc+[(i-1,j)] if anc else [(i-1,j)])
            if is_down(i,j):
                occucp = dc(occu)
                occucp.remove((i+1,j))
                occucp.remove((i+2,j))
                occucp.add((i,j))
                self.do_solve(occucp, anc+[(i+1,j)] if anc else [(i+1,j)])
            if is_left(i,j):
                occucp = dc(occu)
                occucp.remove((i,j-1))
                occucp.remove((i,j-2))
                occucp.add((i,j))
                self.do_solve(occucp, anc+[(i,j-1)] if anc else [(i,j-1)])
            if is_right(i,j):
                occucp = dc(occu)
                occucp.remove((i,j+1))
                occucp.remove((i,j+2))
                occucp.add((i,j))
                self.do_solve(occucp, anc+[(i,j+1)] if anc else [(i,j+1)])
        return

    def solveMarbleSolitaire(self,grid):
        occu,free=set(), set()
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    occu.add((i,j))
                elif grid[i][j] == 0: 
                    free.add((i,j))
                else: pass
        self.alld = occu.union(free)
        print "Total Cell ", self.alld
        self.do_solve(occu, [])

grid=[[-1,-1,1,1,1,-1,-1],
       [-1,1,1,1,1,1,-1],
       [1,1,1,1,1,1,1],
       [1,1,1,0,1,1,1],
       [1,1,1,1,1,1,1],
       [-1,1,1,1,1,1,-1],
       [-1,-1,1,1,1,-1,-1]] 

print Solution().solveMarbleSolitaire(grid)
