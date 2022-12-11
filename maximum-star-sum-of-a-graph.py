class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        g, res, vis = defaultdict(list), -math.inf, set()
        for a,b in edges: _,__=g[a].append(b), g[b].append(a)
        def dfs(r, p):
            nonlocal res
            vis.add(r)
            h, x, cv = [(vals[p] if p >=0 else -math.inf)], 0, 0
            for e in g[r]:
                if e != r and e != p:  h.append(vals[e])
                if e not in vis: dfs(e, r)
            h.sort(reverse=True)
            cv = vals[r]
            while x < k and x < len(h):
                te, x= h[x], x+1
                if te > 0: cv += te
                else: break
            #print('node ', r, 'curr tot', cv, h)
            res = max(res, cv)
        for i in range(len(vals)):
            if i not in vis: dfs(i, -1)
        return res
