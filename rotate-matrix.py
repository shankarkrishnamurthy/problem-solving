import numpy as np
class Solution(object):
    def rotate(self, grid):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def rotate_outer_ring(grid, s, l):
            e = s+l-1
            for i in range(0,l-1):
                t1 = grid[s+i][e]
                grid[s+i][e] = grid[s][s+i]
                t2 = grid[e][e-i]
                grid[e][e-i] = t1
                t3 = grid[e-i][s]
                grid[e-i][s] = t2
                grid[s][s+i] = t3
        
        l = len(grid)
        for k in range(0,l//2):
            #print " Round ", k , l-2*k 
            #print np.array(grid)
            rotate_outer_ring(grid,k,l-2*k)

m1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
m3=[[1,2],[3,4]]
m4=[[1]]
m5=[[]]
Solution().rotate(m1)
print "After: \n", np.array(m1)
Solution().rotate(m2)
print "After: \n", np.array(m2)
Solution().rotate(m3)
print "After: \n", np.array(m3)
Solution().rotate(m4)
print "After: \n", np.array(m4)
Solution().rotate(m5)
print "After: \n", np.array(m5)
