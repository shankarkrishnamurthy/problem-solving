class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if not m: return 1
        n = len(dungeon[0])
        if not n: return 1
        dp = [[1]*(n) for i in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                #To enter i,j = dp[i][j]
                if i == m-1 and j == n-1:
                    dp[i][j] = 1 - dungeon[i][j] if dungeon[i][j] < 1 else 1
                elif i == m-1:
                    # To enter i,j+1 = dp[i][j+1]
                    p1 =  dp[i][j+1] - dungeon[i][j]
                    dp[i][j] = 1 if p1 < 1 else p1
                elif j == n-1:
                    # To enter i+1,j = dp[i+1][j]
                    p1 =  dp[i+1][j] - dungeon[i][j]
                    dp[i][j] = 1 if p1 < 1 else p1
                else:
                    p1 =  dp[i+1][j] - dungeon[i][j]
                    p2 =  dp[i][j+1] - dungeon[i][j]
                    pp = p1 if p1 < p2 else p2
                    dp[i][j] = 1 if pp < 1 else pp
                    
        return dp[0][0]


print Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
print Solution().calculateMinimumHP([[0,0,0],[1,1,-1]])
print Solution().calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]])
