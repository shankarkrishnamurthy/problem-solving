class Solution(object):
    def shortpathBinMaze(self, grid, src, dst):
        res = 0
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        if not n or grid[src[0]][src[1]] == 0: return 0
        q = set([(src[0],src[1])])
        while q:
            cur = set()
            for i,j in q:
                #print i,j, dst
                if (i,j) in [dst]: return res
                grid[i][j] = -1
                if i > 0 and grid[i-1][j] == 1: cur.add((i-1,j))
                if i < len(grid)-1 and grid[i+1][j] == 1: cur.add((i+1,j))
                if j < len(grid)-1 and grid[i][j+1] == 1: cur.add((i,j+1))
                if j > 0 and grid[i][j-1] == 1: cur.add((i,j-1))
            if not cur: return -1
            res += 1
            q = cur
        return -1
            
            
print Solution().shortpathBinMaze([[1,0],[0,1]], (0,0),(1,1))
print Solution().shortpathBinMaze([[1,0],[1,1]], (0,0),(1,1))
print Solution().shortpathBinMaze([[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ], [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ], [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ], [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ], [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ], [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ], [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ], [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]], (0,0), (3,4))
