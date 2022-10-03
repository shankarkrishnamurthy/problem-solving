class Solution:
    def maxSum(self, g):
        m, n, res = len(g), len(g[0]), 0
        for i in range(2,m):
            for j in range(n-2):
                s = g[i][j] + g[i][j+1] + g[i][j+2] + g[i-2][j] + g[i-2][j+1] + g[i-2][j+2] + g[i-1][j+1]
                res = max(res, s)
        return res
