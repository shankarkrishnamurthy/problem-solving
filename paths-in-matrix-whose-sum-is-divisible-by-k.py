class Solution:
    def numberOfPaths(self, g, k):
        m, n = len(g), len(g[0])
        dp, rs = [[[0]*k for __ in range(n)] for _ in range(m)], 0
        for i in range(n):
            rs = (rs + g[0][i]) % k
            dp[0][i][rs] = 1
        rs = 0
        for i in range(m):
            rs = (rs+g[i][0]) % k
            dp[i][0][rs] = 1
        for i in range(1,m):
            for j in range(1,n):
                up, le = dp[i-1][j], dp[i][j-1]
                for p in range(k):
                    dp[i][j][(p+g[i][j]) % k] = (up[p] + le[p]) % 1_000_000_007
        #print('after \n', numpy.array(dp))
        return dp[m-1][n-1][0] % 1_000_000_007
