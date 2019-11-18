import numpy as np
from typing import *
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        print(np.array(grid))
        m,n,res = len(grid),len(grid[0]),0
        hvc = [[(0,0)]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                h = hvc[i][j-1][0]+1 if j > 0 else 1
                v = hvc[i-1][j][1]+1 if i > 0 else 1
                hvc[i][j] = (h,v)
                res = 1
        print(hvc)
        for i in range(m):
            for j in range(n):
                (ch,cv) = hvc[i][j]
                if not (ch > 1 and cv > 1): continue
                ss = min(ch,cv)
                while ss > 1 and ss > res:
                    lc,rc = hvc[i][j-ss+1],hvc[i-ss+1][j]
                    if lc[1] >= ss and rc[0] >= ss: res = max(res,ss)
                    ss-=1
        return res**2
                
                
print(Solution().largest1BorderedSquare(grid = [[0,1,1,1,1,0],[1,1,0,1,1,0],[1,1,0,1,0,1],[1,1,0,1,1,1],[1,1,0,1,1,1],[1,1,1,1,1,1],[1,0,1,1,1,1],[0,0,1,1,1,1],[1,1,1,1,1,1]]))
print(Solution().largest1BorderedSquare(grid = [[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().largest1BorderedSquare(grid = [[1,1,1],[1,1,1],[1,1,0]]))
print(Solution().largest1BorderedSquare(grid = [[1,1,0,0]]))
print(Solution().largest1BorderedSquare(grid = [[1,1,0,0],[1,1,0,0]]))
