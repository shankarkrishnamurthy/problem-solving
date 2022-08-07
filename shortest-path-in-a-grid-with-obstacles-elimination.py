class Solution:
    def shortestPath(self, g, k):
        m, n, q= len(g), len(g[0]), [(0,0,0,0)]
        dp = [[(m*n+1, m*n+1)]*n for _ in range(m)]
        dp[0][0] = (0, 0) # cost, steps
        while q:
            c, s, i, j = heappop(q)
            for a,b in [(i+1,j), (i-1,j), (i, j-1), (i,j+1)]:
                if 0<=a<m and 0<=b<n:
                    (oc, os), nc, ns = dp[a][b], c+g[a][b], s+1
                    if (nc >= oc and ns >= os) or nc > k: continue
                    heappush(q, (nc, ns, a, b) )
                    dp[a][b] = (nc, ns)
        c, s = dp[m-1][n-1]
        return s if c <= k else -1
