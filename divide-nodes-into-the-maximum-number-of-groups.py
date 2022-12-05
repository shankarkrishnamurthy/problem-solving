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
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # return levels or -1 if not bipartite
        def bfs(r, vis):
            lvl, q = 1, [r]
            while q:
                nq = set()
                for i in q:
                    vis.add(i)
                    if i in nq: return -1
                    for e in g[i]:
                        if e not in vis: nq.add(e)
                if not nq: break
                lvl, q = lvl+1, list(nq)
            return lvl
        g, res, uf = defaultdict(list), defaultdict(int), SimpleUnionFind(n+1)
        for i,j in edges: _, __= g[i].append(j), g[j].append(i)
        for i in range(1,n+1):
            vis, x = set(), uf.find(i)
            l = bfs(i ,vis)
            if l == -1: return -1
            if x in res: res[x] = max(res[x], l)
            else:
                for j in vis: uf.union(i, j)
                x = uf.find(i)
                res[x] = l
        return sum(res.values())
