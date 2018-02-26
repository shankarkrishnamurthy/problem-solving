import numpy as np
class Solution(object):
    def maximalRectangle(self, m):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        r = len(m)
        if r == 0: return 0
        c = len(m[0])
        mm = [[(0,0,0,0)]*(c+1) for i in range(r+1)]
        #print np.array(mm)
        maxrect = 0
        for i in range(1,r+1):
            for j in range(1,c+1):
                if m[i-1][j-1] == "0":
                    mm[i][j] = (0,0,0,0)
                    #print "i ",i," j ", j, " tuple ", mm[i][j]
                    continue
                h = mm[i][j-1][0] + 1
                v = mm[i-1][j][1] + 1
                if h == 1:
                    mov = v
                else:
                    mov = max(1,min(mm[i][j-1][3],v))
                if v == 1:
                    moh = h
                else:
                    moh = max(1,min(mm[i-1][j][2],h))
                mm[i][j] = ((h,v,moh,mov))

                hc = h
                for k in range(2,v):
                    hc = min(hc, mm[i-k+1][j][0])
                    if moh >= hc: break
                    maxrect = max(maxrect, hc*k)

                maxrect = max(maxrect, mov*h, moh*v)
                #print "i ",i," j ", j, " tuple ", mm[i][j]
        #print np.array(mm)
        return maxrect

print Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print Solution().maximalRectangle([["1","0","1","1","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","1","1","0"]])
print Solution().maximalRectangle([["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]])
print Solution().maximalRectangle([["0","0","1"],["0","1","1"],["1","1","1"]])

