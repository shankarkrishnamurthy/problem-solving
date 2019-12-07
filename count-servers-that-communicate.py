from typing import *
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        r,c,cnt,res = {},{},0,0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]: continue
                r.setdefault(i,[]).append((i,j))
                c.setdefault(j,[]).append((i,j))
                cnt += 1
        for i in r:
            if len(r[i]) > 1: continue
            if len(c[r[i][0][1]]) > 1: continue
            res += 1
        return cnt - res

print(Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))
print(Solution().countServers([[1,0],[1,1]]))
print(Solution().countServers([[1,0],[0,1]]))
