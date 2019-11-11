from typing import *
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        g = [[0]*m for _ in range(n)]
        for i in indices:
            r,c=i[0],i[1]
            for a in range(m): g[r][a] += 1
            for a in range(n): g[a][c] += 1
        return sum([g[i][j]%2 for i in range(n) for j in range(m)])
        

print(Solution().oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
print(Solution().oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))
