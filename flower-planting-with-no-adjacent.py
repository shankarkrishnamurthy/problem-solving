class Solution(object):
    def gardenNoAdj(self, N, p):
        """
        :type N: int
        :type p: List[List[int]]
        :rtype: List[int]
        """
        h = {}
        for i in p:
            x,y = i[0],i[1]
            h.setdefault(i[0],[]).append(i[1])
            h.setdefault(i[1],[]).append(i[0])
        #print h
        g = [0]*N
        for i in xrange(N):
            if i+1 in h: 
                rs = {1,2,3,4} - {g[j-1] for j in h[i+1]}
                g[i] = rs.pop()
            else: g[i] = 1
        return g

print Solution().gardenNoAdj(5,[[3,4],[4,5],[3,2],[5,1],[1,3],[4,2]])
print Solution().gardenNoAdj(4,[[3,4],[4,2],[3,2],[1,3]])
print Solution().gardenNoAdj(1, [] )
print Solution().gardenNoAdj(3, [[1,2],[2,3],[3,1]])
print Solution().gardenNoAdj(4, [[1,2],[3,4]])
print Solution().gardenNoAdj(4, [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]])
