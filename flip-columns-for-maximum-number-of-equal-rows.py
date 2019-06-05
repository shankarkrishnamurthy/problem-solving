class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n,h = len(matrix[0]),{}
        a = set(x for x in xrange(n))
        for r in matrix:
            s=tuple(i for i,j in enumerate(r) if j == 1)
            s1=tuple(a-set(s))
            h[s] = h.get(s,0) + 1
            h[s1] = h.get(s1,0) + 1
            #print 'R', r,'H', h, 'S',s,'S1', s1
        return max(h.values())

print Solution().maxEqualRowsAfterFlips( [[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,0,0,0,1,1,1,0,1,1,1],[1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,1,1,0,1,1,1]])
#print Solution().maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]])
#print Solution().maxEqualRowsAfterFlips([[0,1],[1,0]])
#print Solution().maxEqualRowsAfterFlips([[0,1],[1,1]])
#print Solution().maxEqualRowsAfterFlips([[0]])
