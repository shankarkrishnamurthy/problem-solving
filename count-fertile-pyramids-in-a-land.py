#import numpy as np
class Solution:
    def countPyramids(self, g):
        m,n, res = len(g), len(g[0]), 0
        dp, dpi = [[0]*n for i in range(m)], [[0]*n for i in range(m)]
        for i in range(m-2,-1,-1):
            for j in range(1,n-1):
                if g[i][j]:
                    if g[i+1][j-1] and g[i+1][j] and g[i+1][j+1]: dp[i][j] += 1
                    dp[i][j] += min(dp[i+1][j-1], dp[i+1][j],dp[i+1][j+1])
                
        for i in range(1,m):
            for j in range(1,n-1):
                if g[i][j]:
                    if g[i-1][j-1] and g[i-1][j] and g[i-1][j+1]: dpi[i][j] += 1
                    dpi[i][j] += min(dpi[i-1][j-1], dpi[i-1][j],dpi[i-1][j+1])
                    
        for i in range(m): res += sum(dp[i]) + sum(dpi[i])
        #print(np.array(dp),'\n', np.array(dpi))
        return res
