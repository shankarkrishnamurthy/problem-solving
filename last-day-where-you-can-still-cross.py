import copy
class Solution:
    def latestDayToCross(self, row, col, cl):
        def fill(k):
            for i in range(k):
                (x,y) = cl[i]
                g[x-1][y-1] = 1
        def walk(x, y):
            if x == row-1: return True
            g[x][y] = 2
            for a,b in [(x+1,y), (x,y+1), (x,y-1),(x-1,y)]:
                if 0<=a<row and 0<=b<col and g[a][b] == 0: 
                    if walk(a,b): return True
            return False
        l, r = 0, row*col
        while l < r:
            m, rc = (l+r)//2, False
            g = [[0]*col for i in range(row)]
            fill(m)
            for j in range(col):
                if g[0][j] == 0 and walk(0, j): 
                    rc=True
                    break
            if not rc: r = m
            else: l = m + 1
        return r-1
    
    
