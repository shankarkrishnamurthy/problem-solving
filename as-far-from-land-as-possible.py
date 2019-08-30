class Solution(object):
    def maxDistance(self, g):
        """
        :type g: List[List[int]]
        :rtype: int
        """
        q,c,n = set(),0,len(g)
        for i in xrange(n):
            for j in xrange(n):
                if g[i][j]: q.add((i,j)) 
        if not q or len(q)==n*n: return -1
        while q:
            t = set()
            for i,j in q:
                g[i][j] = -1
                for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0<=x<n and 0<=y<n and g[x][y] == 0 and (x,y) not in q:
                        t.add((x,y))

            if not t: return c
            c += 1
            q = t
        return c

print Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
print Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]])
