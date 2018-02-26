import numpy as np
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        print grid
        r = len(grid)
        if r==0 or r and not grid[0]:
            return 0
        c = len(grid[0])
        if r > 1:
            for i in range(1,r):
                grid[i][0] += grid[i-1][0]
        if c > 1:
            for i in range(1,c):
                grid[0][i] += grid[0][i-1]
        for i in range(1,r):
            for j in range(1,c):
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])
        return grid[r-1][c-1]

print Solution().minPathSum([[]])
print Solution().minPathSum([[1]])
print Solution().minPathSum([[1],[2],[3]])
print Solution().minPathSum([[1,2,3]])
print Solution().minPathSum([[1,3,1], [1,5,1], [4,2,1]])
