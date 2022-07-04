from heapq import *
class Solution:
    def minCost(self, g):
        mv, m, n = sys.maxsize, len(g), len(g[0])
        dp, cf=[[mv]*n for i in range(m)], {1:(0,1), 2:(0,-1),3:(1,0),4:(-1,0)}
        q, dp[0][0] = [(0,(0,0))], 0
        while q:
            k, (i,j) = heappop(q)
            if (i,j)==(m-1,n-1): return k
            #print(((i,j),'k',k))
            dx,dy = cf[g[i][j]]
            if 0<=i+dx<m and 0<=j+dy<n and k < dp[i+dx][j+dy]:
                dp[i+dx][j+dy] = k
                heappush(q, (k, (i+dx,j+dy)))
            for a,b in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]:
                if (i+dx,j+dy)!=(a,b) and 0<=a<m and 0<=b<n and k+1 < dp[a][b]:
                    dp[a][b] = k+1
                    heappush(q, (k+1, (a,b)))
        return dp[m-1][n-1]
