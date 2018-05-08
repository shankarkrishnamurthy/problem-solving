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
        global maxnv
        def walk_grid(grid, row, col):
            global maxnv
            if dp[row][col] or grid[row][col] == 0: return 0
            dp[row][col] = island
            def get_max(m):
                if not m: return 0
                #print row,col,m, maxnv
                return sum([islandcellmap[x] for x in m])
            if col > 0 and grid[row][col-1] == 0:
                maxneigh = set()
                if col > 1 and grid[row][col-1] == 0: maxneigh.add(dp[row][col-2])
                if row > 0: maxneigh.add(dp[row-1][col-1])
                if row < len(grid)-1:maxneigh.add(dp[row+1][col-1])
                maxnv = max(maxnv, get_max(maxneigh-set([0,island])))
            if col < len(grid[0])-1 and grid[row][col+1] == 0:
                maxneigh = set()
                if col < len(grid[0])-2 and grid[row][col+1] == 0: maxneigh.add(dp[row][col+2])
                if row > 0: maxneigh.add(dp[row-1][col+1])
                if row < len(grid)-1:maxneigh.add(dp[row+1][col+1])
                maxnv = max(maxnv, get_max(maxneigh-set([0,island])))
            if row < len(grid)-1 and grid[row+1][col] == 0:
                maxneigh = set()
                if row < len(grid)-2: maxneigh.add(dp[row+2][col])
                if col > 0: maxneigh.add(dp[row+1][col-1])
                if col < len(grid[0])-1: maxneigh.add(dp[row+1][col+1])
                maxnv = max(maxnv, get_max(maxneigh-set([0,island])))
            if row > 0 and grid[row-1][col] == 0:
                maxneigh = set()
                if row > 1: maxneigh.add(dp[row-2][col])
                if col > 0: maxneigh.add(dp[row-1][col-1])
                if col < len(grid[0])-1: maxneigh.add(dp[row-1][col+1])
                maxnv = max(maxnv, get_max(maxneigh-set([0,island])))
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
                    maxnv = 0
                    islandcellmap[island] = walk_grid(grid, i, j)
                    msf = min(m*n,max(msf, maxnv+1+islandcellmap[island]))
        #print np.array(dp)
        return msf

print Solution().largestIsland([[1,0,0],[0,1,1],[0,0,1]])
print Solution().largestIsland([[1,0],[0,1]])
print Solution().largestIsland([[1,1],[0,1]])
print Solution().largestIsland([[1,1],[1,1]])
print Solution().largestIsland([[0,0],[0,0]])
print Solution().largestIsland([[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,1,0,0,1,0,0],[1,0,1,0,1,0,0],[0,1,0,0,1,0,0],[0,1,0,0,1,0,0],[0,1,1,1,1,0,0]])
print Solution().largestIsland([[0,1,1,1,1,0],[0,1,1,1,1,1],[0,0,0,0,0,1],[1,0,0,1,0,0],[1,0,0,1,0,1],[0,1,1,0,1,0]])
