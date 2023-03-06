class Solution:
    def rootCount(self, el, gl, k):
        n, gs, vis, g = len(el), {tuple(i) for i in gl}, set(), defaultdict(list)
        for a,b in el: _, __ = g[a].append(b), g[b].append(a)
        def dfs(i, p):
            vis.add(i)
            t = 0
            for c in g[i]:
                if c in vis: continue
                t += dfs(c, i) + ((i, c) in gs)
            return t
        t = dfs(0, -1)
        res, vis = 0, set()
        def dfs2(i, t):
            nonlocal res
            vis.add(i)
            res += (t >= k)
            for c in g[i]:
                if c in vis: continue
                nt = t - ((i,c) in gs) + ((c, i) in gs)
                dfs2(c, nt)
        dfs2(0, t)
        return res
