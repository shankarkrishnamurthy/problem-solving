class Solution(object):
    def orangesRotting(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(g)
        n = len(g[0])
        cnt,tot,q = 0,0,set()
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0: continue
                if g[i][j] == 2: q.add((i,j))
                tot += 1
        visit = set()
        while q:
            cur = set()
            for (i,j) in q:
                visit.add((i,j))
                for (k,l) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=k<m and 0<=l<n: 
                        if (k,l) not in visit and (k,l) not in q and g[k][l] == 1:
                            cur.add((k,l))
            if not cur: break
            q = cur
            cnt += 1
            print visit, q
        return cnt if tot == len(visit) else -1

#print Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
#print Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
#print Solution().orangesRotting([[0,2]])
print Solution().orangesRotting([[2,2],[1,1],[0,0],[2,0]])
