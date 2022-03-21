import math
from heapq import *
class Solution:
    def minimumWeight(self, n, el, s1, s2, dst):
        def dijkstra(G, sn):
            q, res, vis= [(0, sn)], [float("inf")]*n, set()
            while q:
                w,v = heappop(q)
                if v in vis: continue
                res[v] = min(res[v],w)
                vis.add(v)
                if v not in G: continue
                for (dn,wi) in G[v]:
                    if dn not in vis: heappush(q, (wi + w,dn))
            return res
        g, grev= {}, {}
        for v in el:
            g.setdefault(v[0],[]).append((v[1],v[2]))
            grev.setdefault(v[1],[]).append((v[0],v[2]))
        r1, r2, r3, res = dijkstra(g, s1), dijkstra(g, s2), dijkstra(grev, dst), float("inf")
        for i in range(n): 
            res = min(res, r1[i] + r2[i] + r3[i])
        return -1 if math.isinf(res) else res
