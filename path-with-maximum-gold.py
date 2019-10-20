import numpy as np
from typing import *
class Solution:
    def __init__(self):
        self.ans = 0
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i,j,v,ss):
            ss += grid[i][j]
            v.add((i,j))
            for a,b in [(i,j+1),(i,j-1),(i-1,j),(i+1,j)]:
                if 0<=a<m and 0<=b<n and grid[a][b] > 0 and (a,b) not in v:
                    dfs(a,b,v,ss)
            v.remove((i,j))
            self.ans = max(ss,self.ans)

        print(np.array(grid))
        m,n,v = len(grid), len(grid[0]),set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] > 0: dfs(x,y,v,0)
        return self.ans

print(Solution().getMaximumGold(grid=[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(Solution().getMaximumGold(grid=[[0,6,0],[5,8,7],[0,9,0]]))
print(Solution().getMaximumGold(grid=[[0,0,0,0,0,0,32,0,0,20],[0,0,2,0,0,0,0,40,0,32],[13,20,36,0,0,0,20,0,0,0],[0,31,27,0,19,0,0,25,18,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,18,0,6],[0,0,0,25,0,0,0,0,0,0],[0,0,0,21,0,30,0,0,0,0],[19,10,0,0,34,0,2,0,0,27],[0,0,0,0,0,34,0,0,0,0]]))
