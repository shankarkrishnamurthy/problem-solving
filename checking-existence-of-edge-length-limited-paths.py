class UnionFind():
    def __init__(o, N):
        o._par, o._wgt = list(range(N)), [1]*N
    def find(o, v1):
        while v1 != o._par[v1]: v1 = o._par[v1]
        return v1
    def union(o, v1, v2):
        r1, r2 = o.find(v1), o.find(v2)
        if r1 == r2: return
        if o._wgt[r1] < o._wgt[r2]: r1, r2 = r2, r1
        o._wgt[r1], o._par[r2] = o._wgt[r1] + o._wgt[r2], r1
    def print(o, msg): print(msg, 'uf',o._par, 'wgt', o._wgt, end=' ')
class Solution:
    def distanceLimitedPathsExist(self, n, el, ql):
        ih={tuple(v):i for i,v in enumerate(ql)}
        el.sort(key=lambda x:x[2]), ql.sort(key=lambda x:x[2])
        res, l, uf = [True]*len(ql), 0, UnionFind(n)
        for (v1,v2,li) in ql:
            while l < len(el) and el[l][2] < li:
                (a, b, _), l = el[l], l+1
                uf.union(a,b)
            if uf.find(v1) != uf.find(v2): res[ih[(v1,v2,li)]]=False
            #uf.print((v1,v2,li)), print(l, 'idx', ih[(v1,v2,li)], res[ih[(v1,v2,li)]])
        return res
