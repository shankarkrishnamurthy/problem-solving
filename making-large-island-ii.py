import numpy as np
class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #print np.array(grid)    
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])
        # dp contains island id of each coordinate
        dp=[[0]*m for _ in range(n)]
        # Island ID to Count of cell mapping
        islandcellmap={0:0}
        island,msf = 0,1
        def walk_grid(grid, row, col):
            if dp[row][col] or grid[row][col] == 0: return 0
            dp[row][col] = island
            d,r,u,l = 0,0,0,0
            if row+1 < len(grid): d = walk_grid(grid,row+1,col)
            if col+1 < len(grid[0]): r = walk_grid(grid,row,col+1)
            if row-1 >=0: u = walk_grid(grid,row-1,col)
            if col-1 >=0: l = walk_grid(grid,row,col-1)
            return d+r+l+u+1
            
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0 and grid[i][j] == 1:
                    island += 1
                    islandcellmap[island] = walk_grid(grid, i, j)
        msf = islandcellmap[1] if islandcellmap.has_key(1) else 1
        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0:
                    def get_max(m):
                        if not m: return 0
                        print i,j,m, msf
                        return sum([islandcellmap[x] for x in m])
                    neighset = set()
                    if i > 0: neighset.add(dp[i-1][j])
                    if i < m-1: neighset.add(dp[i+1][j])
                    if j > 0: neighset.add(dp[i][j-1])
                    if j < n-1: neighset.add(dp[i][j+1])
                    msf = max(msf, 1+get_max(neighset))
        print np.array(dp)
        return msf

print Solution().largestIsland([[1,0,0],[0,1,1],[0,0,1]])
print Solution().largestIsland([[1,0],[0,1]])
print Solution().largestIsland([[1,1],[0,1]])
print Solution().largestIsland([[1,1],[1,1]])
print Solution().largestIsland([[0,0],[0,0]])
print Solution().largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]])
print Solution().largestIsland([[0,1,1,1,1,0],[0,1,1,1,1,1],[0,0,0,0,0,1],[1,0,0,1,0,0],[1,0,0,1,0,1],[0,1,1,0,1,0]])
