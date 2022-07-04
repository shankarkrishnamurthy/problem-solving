class SimpleUnionFind():
    def __init__(o, N):
        o.p = list(range(N))
        o.w = [1]*N
    def find(o, x):
        while o.p[x] != x: x = o.p[x]
        return x
    def union(o,a,b):
        x,y = o.find(a), o.find(b)
        if x == y: return
        if o.w[x] < o.w[y]: x,y = y, x
        o.p[y], o.w[x] = x, o.w[x]+o.w[y] # 'x' is bigger
class Solution:
    def maxNumEdgesToRemove(self, n, el):
        uf1, uf2, blue, A, B=SimpleUnionFind(n+1), SimpleUnionFind(n+1), 0, 0, 0
        for t,i,j in el:
            if t == 3 and uf1.find(i) != uf1.find(j): 
                uf1.union(i,j), uf2.union(i,j)
                blue += 1
        for t,i,j in el:
            if t == 3: continue
            if t==1 and uf1.find(i) != uf1.find(j):
                uf1.union(i,j)
                A+=1
            if t==2 and uf2.find(i) != uf2.find(j):
                uf2.union(i,j)
                B+=1
        if blue+A != n-1 or blue+B != n-1: return -1
        #print(blue, A, B)
        return len(el) - blue - A - B
