from copy import deepcopy
class Solution:
    def minPathCost(self, g, mc):
        m,n,dp = len(g), len(g[0]),deepcopy(g)
        for i in range(1, m):
            for j in range(n):
                crow = float("inf")
                for k in range(n): crow = min(crow, dp[i-1][k] + mc[g[i-1][k]][j])
                dp[i][j] += crow
        return min(dp[m-1])
