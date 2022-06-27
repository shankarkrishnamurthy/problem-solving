class Solution:
    def countPairs(self, n, edges):
        g=defaultdict(list)
        for (i,j) in edges:
            g.setdefault(i, []).append(j)
            g.setdefault(j, []). append(i)
        def dfs(i, v):
            if i in v: return
            v.add(i)
            for j in g[i]: dfs(j, v)
            return
        v, res = set(), 0
        for i in range(n):
            if i not in v: 
                p = len(v)
                dfs(i, v)
                res += (len(v) - p) * (n - len(v))
        return res
        
