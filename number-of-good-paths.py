class UnionFind():
    def __init__(o, N):
        o.p, o.w = list(range(N)), [1]*N
    def find(o, x):
        while o.p[x] != x: x = o.p[x]
        return x
    def union(o,a,b):
        x,y = o.find(a), o.find(b)
        if x==y: return
        if o.w[x] < o.w[y]: x,y = y, x
        o.p[y], o.w[x] = x, o.w[x]+o.w[y]
class Solution:
    def numberOfGoodPaths(self, vals, edges):
        g, vh = defaultdict(list), defaultdict(list)
        for i,v in enumerate(vals): vh[v].append(i)
        for a,b in edges: _, __ = g[a].append(b), g[b].append(a)
        vis, res, uf = set(), len(vals), UnionFind(len(vals))
        for v in sorted(vh):
            nl, rh = vh[v], defaultdict(int)
            for i in nl:
                vis.add(i)
                for e in g[i]:
                    if e in vis: uf.union(i, e)
            for i in nl: rh[uf.find(i)] += 1
            for r in rh: res += rh[r]*(rh[r]-1)//2
        return res
