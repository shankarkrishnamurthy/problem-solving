import numpy as np
from copy import deepcopy as dc
class Solution(object):
    def knightProbability(self, N, K, r, c):
        n = max(4*K + r+5,4*K + c+5)
        prev = [[0]*n for i in range(n)]
        ox,oy = 2*K+r+1,2*K+c+1
        print n, (ox,oy)
        prev[ox][oy] = 1
        for k in range(0,K):
            dp = [[0]*n for i in range(n)]
            for i in range(0,n):
                for j in range(0,n):
                    l = [(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1),(i-1,j-2),(i-1,j+2 ),(i+1,j-2),(i+1,j+2)]
                    for (ci,cj) in l:
                        if ci < n and cj < n and ci >=0 and cj >=0 and prev[ci][cj] > 0: 
                            dp[i][j] += 1
            prev=dc(dp)
            print np.array(dp)
        numer,denom = 0,0
        for i in range(n):
            for j in range(n):
                if dp[i][j] > 0: denom += dp[i][j]

        for i in range(ox,ox+N):
            for j in range(oy,oy+N):
                if dp[i][j] > 0: numer += dp[i][j]

        print numer,denom
        return float(numer)/float(denom)

print Solution().knightProbability(3,2,0,0)
