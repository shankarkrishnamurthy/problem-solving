class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n,peri = len(grid), len(grid[0]),0
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or (i >0 and grid[i-1][j] == 0): peri += 1
                    if i == m-1 or (i < m-1 and grid[i+1][j] == 0): peri += 1
                    if j == n-1 or (j < n-1 and grid[i][j+1] == 0): peri += 1
                    if j == 0 or (j >0 and grid[i][j-1] == 0): peri += 1
        
        return peri

print Solution().islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]])
print Solution().islandPerimeter([[1,1],[1,1]])
print Solution().islandPerimeter([[1]])
