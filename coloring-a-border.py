class Solution(object):
    def colorBorder(self, g, r0, c0, color):
        """
        :type g: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        self.bdr = set()
        def dfs(g,i,j,v):
            if (i,j) in v: return
            v.add((i,j))
            for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <=a<m and 0<=b<n and g[a][b] == myc:
                    dfs(g,a,b,v)
                else: self.bdr.add((i,j))
            return

        myc = g[r0][c0]
        if myc == color: return g
        m,n = len(g), len(g[0])
        dfs(g,r0,c0,set())
        for i,j in self.bdr: g[i][j] = color
        return g

print Solution().colorBorder([[1,1],[1,2]], 0, 0, 3)
print Solution().colorBorder([[1,2,2],[2,3,2]], 0, 1, 3)
print Solution().colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2)
