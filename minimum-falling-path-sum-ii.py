class Solution:
    def minFallingPathSum(self, g):
        if len(g) == 1: return g[0][0]
        dp=[(-1,0)]
        for i, row in enumerate(g):
            ndp=[]
            for j,v in enumerate(row):
                if dp[0][0] != j: ndp.append((j,v+dp[0][1]))
                else: ndp.append((j,v+dp[1][1]))
            dp = sorted(ndp, key=lambda x: x[1])[:2]
        return dp[0][1]
