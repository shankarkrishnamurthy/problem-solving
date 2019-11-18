from typing import *
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        la = [j for i in grid for j in i]
        la += la
        k = k % (m*n)
        s = m*n-k
        def convMat(a,n):
            ret,i = [],0
            while i < len(a):
                r = []
                for c in range(n):
                    r.append(a[i])
                    i+=1
                ret.append(r)
            return ret
        
        return convMat(la[s:s+m*n],n)
        

print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))
print(Solution().shiftGrid(grid = [[1]], k = 9))
print(Solution().shiftGrid(grid = [[1,2]], k = 9))
