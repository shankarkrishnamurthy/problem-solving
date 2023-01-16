class Solution:
    def maxOutput(self, n, edges, pr):
        @lru_cache(None)
        def walk(i, p):
            cp = []
            for e in g[i]:
                if e != p:
                    cp.append(walk(e, i))
            return pr[i] + (max(cp) if len(cp) > 0 else 0)
        g, res = defaultdict(list), 0
        for a,b in edges: _, __ = g[a].append(b), g[b].append(a)
        for i in range(n): 
            res = max(res, walk(i, -1) - pr[i])
        return res
