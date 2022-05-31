class Solution:
    def minimumObstacles(self, g):
        m,n = len(g), len(g[0])
        q, dp, gh = [(0,0,0)], [[-1]*n for i in range(m)], {(0,0): 0}
        while q:
            (c,i,j) = heappop(q)
            #print('q', q)
            dp[i][j] = c
            if i == m-1 and j == n-1: return c
            for a,b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if not (0<=a<m and 0<=b<n and dp[a][b] == -1): continue
                if (a,b) in gh and gh[(a,b)] <= c+g[a][b]: continue
                gh[(a,b)] = c+g[a][b]
                heappush(q, (gh[(a,b)], a,b))
