class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check_grid(i,j):
            th,r,c = {},0,0
            r1 = grid[i][j] + grid[i+1][j] + grid[i+2][j]
            c1 = grid[i][j] + grid[i][j+1] + grid[i][j+2]
            d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            for x in range(3):
                a,c = i+x,0
                for y in range(3):
                    b = j+y
                    th[grid[a][b]] = th.get(grid[a][b],0) + 1
            if th != h: return 0
            if r1 !=c1 or r1 != d1: return 0
            return 1

        m = len(grid)
        if m < 3: return 0
        n,s = len(grid[0]),0
        if n < 3: return 0
        h = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
        for i in range(m-2):        
            for j in range(n-2):        
                if check_grid(i,j): s += 1
        return s

print Solution().numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]])
