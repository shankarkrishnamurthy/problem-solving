# 2d difference array
class Solution:
    def rangeAddQueries(self, n, q):
        g = [[0]*n for _ in range(n)]
        for a,b,x,y in q:
            g[a][b] += 1
            if x < n-1: g[x+1][b] -= 1
            if y < n-1: g[a][y+1] -= 1
            if x < n-1 and y < n-1: g[x+1][y+1] += 1
        for i in range(n):
            for j in range(n):
                l = g[i-1][j] if i > 0 else 0
                r = g[i][j-1] if j > 0 else 0
                d = g[i-1][j-1] if i >0 and j > 0 else 0
                g[i][j] += l + r - d
        return g
