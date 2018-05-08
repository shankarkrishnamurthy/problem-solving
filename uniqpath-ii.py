class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if not m: return 0
        n = len(obstacleGrid[0])
        if not n: return 0
        dp = [[0]*n for i in range(m)]
        if obstacleGrid[0][0] == 1: return 0
        dp[0][0] = 1
        for i in range(1,m): 
            if obstacleGrid[i][0] == 1: continue
            dp[i][0] = dp[i-1][0]
        for j in range(1,n): 
            if obstacleGrid[0][j] == 1: continue
            dp[0][j] = dp[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1: continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

print Solution().uniquePathsWithObstacles([ [0,0,0], [0,1,0], [0,0,0] ])
        
