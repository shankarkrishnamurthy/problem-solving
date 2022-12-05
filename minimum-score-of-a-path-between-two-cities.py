class SimpleUnionFind():
    def __init__(o, N):
        o.p,o.w = list(range(N)), [1]*N
    def find(o, x):
        while o.p[x] != x: x = o.p[x]
        return x
    def union(o,a,b):
        x,y = o.find(a), o.find(b)
        if x==y: return
        if o.w[x] < o.w[y]: x,y = y, x
        o.p[y], o.w[x] = x, o.w[x]+o.w[y]
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf, mh = SimpleUnionFind(n+1), {i: math.inf for i in range(n+1)}
        for i,j,w in roads:
            a = min(mh[uf.find(i)], mh[uf.find(j)])
            uf.union(i,j)
            mh[uf.find(i)] = min(a,w)
        return mh[uf.find(1)]
