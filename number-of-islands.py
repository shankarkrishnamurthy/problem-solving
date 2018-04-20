class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def walk_grid(grid, row, col, dp):
            if dp[row][col] or grid[row][col] == '0': return
            dp[row][col] = True
            nr = row + 1
            nc = col + 1
            if nr < len(grid): walk_grid(grid,nr,col,dp)
            if nc < len(grid[0]): walk_grid(grid,row,nc,dp)
            pr = row-1
            pc = col-1
            if pr >=0: walk_grid(grid,pr,col,dp)
            if pc >=0: walk_grid(grid,row,pc,dp)
            return
            
        if not grid: return 0
        n = len(grid)
        m = len(grid[0])
        dp=[[False]*m for _ in range(n)]
        island = 0
        for i in range(n):
            for j in range(m):
                if not dp[i][j] and grid[i][j] == '1':
                    island += 1
                    walk_grid(grid, i, j, dp)
        return island
        
print Solution().numIslands([['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']])
print Solution().numIslands([['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']])
print Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]])
