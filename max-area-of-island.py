class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def do_dfs(i,j):
            visit.add((i,j))
            u,l,d,r = 0,0,0,0
            if i > 0 and grid[i-1][j] == 1 and (i-1,j) not in visit: u = do_dfs(i-1,j)
            if j > 0 and grid[i][j-1] == 1 and (i,j-1) not in visit: l = do_dfs(i,j-1)
            if i < m-1 and grid[i+1][j] == 1 and (i+1,j) not in visit: d = do_dfs(i+1,j)
            if j < n-1 and grid[i][j+1] == 1 and (i,j+1) not in visit: r = do_dfs(i,j+1)
            return l+r+d+u+1

        visit,ma = set(), 0
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n: return 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visit:
                    ma = max(ma, do_dfs(i,j))

        return ma

print Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0], [0,1,0,0,1,1,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,1,1,0,0,0,0]])
print Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]])
