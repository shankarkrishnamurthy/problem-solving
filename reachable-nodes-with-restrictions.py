class Solution:
    def reachableNodes(self, n, el, rl):
        rs, g, res, v = set(rl), [[] for _ in range(n)], 0, set()
        for a,b in el:
            g[a].append(b), g[b].append(a)
        def dfs(i):
            v.add(i)
            s = 0
            for k in g[i]:
                if k not in rs and k not in v: s += dfs(k)
            return s+1
        return dfs(0)
