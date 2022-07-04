class Solution:
    def countPaths(self, g):
        m,n, mod = len(g), len(g[0]), 10**9+7
        dp=[[-1]*n for i in range(m)]
        
        def dfs(i,j):
            if dp[i][j] != -1: return dp[i][j]
            tot, v = 1, g[i][j]
            if i > 0 and g[i-1][j] < v: tot += dfs(i-1, j)
            if i < m-1 and g[i+1][j] < v: tot += dfs(i+1, j)
            if j > 0 and g[i][j-1] < v: tot += dfs(i, j-1)
            if j < n-1 and g[i][j+1] < v: tot += dfs(i, j+1)
            dp[i][j] = tot % mod
            return tot
        for i in range(m):
            for j in range(n):
                if dp[i][j] == -1: dfs(i,j)
        #print(dp)
        return sum([sum(dp[r]) for r in range(m)]) % mod
