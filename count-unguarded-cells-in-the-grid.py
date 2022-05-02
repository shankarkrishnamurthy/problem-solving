class Solution:
    def countUnguarded(self, m,n, g,w):
        def register(a,b):
            gc.add((a,b))
            return (True if ((a,b) in ws or (a,b) in gs) else False)
        def addcell(i,j):
            c=1
            gc.add((i,j))
            while j+c < n: 
                y, c = j+c, c+1
                if register(i,y): break
            c=1
            while j-c >= 0:
                y, c = j-c, c+1
                if register(i,y): break
            c=1
            while i+c < m:
                x, c = i+c, c+1
                if register(x,j): break
            c=1
            while i-c >= 0:
                x, c = i-c, c+1
                if register(x,j): break
        gs, ws, gc = set(map(tuple, g)), set(map(tuple, w)), set(map(tuple, w))
        for i,j in g: addcell(i,j)
        return m*n - len(gc)
