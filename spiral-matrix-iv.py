class Solution:
    def spiralMatrix(self, m,n,h):
        dp, vis, c, dr, mx=[[-1]*n for i in range(m)], set(), (0,0), 0, m*n
        dl = [(0,1),(1,0),(0,-1),(-1,0)]
        while h:
            v, (a,b) = h.val, c
            vis.add((a,b))
            dp[a][b], na, nb = v, a+dl[dr][0], b+dl[dr][1]
            if len(vis) == mx: break
            while not (0<=na<m and 0<=nb<n and (na,nb) not in vis):
                dr = (dr+1)%4
                na, nb = a+dl[dr][0], b+dl[dr][1]
            c, h = (na,nb), h.next
        return dp
