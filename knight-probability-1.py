import numpy as np
class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0]*N for _ in range(N)]
        dp[r][c] = 1
        for h in range(K):
            dp2 = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    moves = [(i-2,j-1),(i-2,j+1),(i+2,j-1),(i+2,j+1),(i-1,j-2),(i-1,j+2),(i+1,j-2),(i+1,j+2)]
                    for mi,mj in moves:
                        if mi >=0 and mj >= 0 and mi < N and mj < N:
                            dp2[mi][mj] += float(dp[i][j])/8.0
            print np.array(dp2)
            dp = dp2
        return sum(map(sum, dp))
        
print Solution().knightProbability(3,2,0,0)
