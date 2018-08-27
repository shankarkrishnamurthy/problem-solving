class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sfarea = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if v > 0: sfarea += 2
                # up
                if i == 0: sfarea += v 
                else: sfarea += v-grid[i-1][j] if v > grid[i-1][j] else 0
                #left
                if j == 0: sfarea += v
                else: sfarea += v - grid[i][j-1] if v > grid[i][j-1] else 0
                #down
                if i == m-1: sfarea += v 
                else: sfarea += v-grid[i+1][j] if v > grid[i+1][j] else 0
                #right
                if j == n-1: sfarea += v
                else: sfarea += v - grid[i][j+1] if v > grid[i][j+1] else 0
        return sfarea
        

print Solution().surfaceArea([[2]])
print Solution().surfaceArea([[1,2],[3,4]])
print Solution().surfaceArea([[1,0],[0,2]])
print Solution().surfaceArea([[1,1,1],[1,0,1],[1,1,1]])
print Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]])
