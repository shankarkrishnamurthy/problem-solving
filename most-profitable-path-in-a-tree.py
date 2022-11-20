class Solution:
    def mostProfitablePath(self, edges, bob, amt):
        res, g, pa, vis = float("-inf"), defaultdict(list), [0]*len(amt), set()
        for a,b in edges: _, __ = g[a].append(b), g[b].append(a)
        def palist(r):
            vis.add(r)
            for e in g[r]:
                if e not in vis: 
                    pa[e] = r
                    palist(e)
        palist(0)
        ba, tmp, vis = [], bob, set()
        while tmp != 0:
            ba.append(tmp)
            tmp = pa[tmp]
        ba.append(0)
        for i in range(len(ba)//2): amt[ba[i]] = 0
        if len(ba) % 2 == 1: 
            mid = ba[len(ba)//2]
            amt[mid] = amt[mid]//2
        def dfs(r, tot):
            nonlocal res
            vis.add(r)
            tot += amt[r]
            nch = False
            for e in g[r]:
                if e not in vis:
                    nch = True
                    dfs(e, tot)
            if not nch: res = max(res, tot)
            tot -= amt[r]
        dfs(0, 0)
        return res
