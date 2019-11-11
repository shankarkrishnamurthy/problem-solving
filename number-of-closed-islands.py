import numpy as np
from typing import *
class Solution:
    def __init__(self):
        self.cc = False
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,grid):
            if (i==m-1 or j ==n-1 or i==0 or j == 0) and grid[i][j] == 0: self.cc = False
            rc,grid[i][j] = True, 2
            for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if not (0<=x<m and 0<=y<n): continue
                if grid[x][y] == 0: rc &= dfs(x,y,grid)
            return self.cc
        
        rc,m,n = 0,len(grid),len(grid[0])
        #print(np.array(grid))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.cc = True
                    rc += dfs(i,j,grid)
                    #print (i,j,np.array(grid),'rc', rc)
        return rc

print(Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))
print(Solution().closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
print(Solution().closedIsland([[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[0,1,1,1,0]]))
print(Solution().closedIsland([[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]]))
