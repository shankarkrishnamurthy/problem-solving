class Solution:
    def maximumScore(self, sc, edges):
        def addedge(v1,v2):
            g.setdefault(v1, [])
            g.setdefault(v2, [])
            insort(g[v1], (-sc[v2], v2))
            insort(g[v2], (-sc[v1], v1))
            if len(g[v1]) > 3: g[v1].pop()
            if len(g[v2]) > 3: g[v2].pop()
                
        g, msf = {}, -1
        for v1,v2 in edges: addedge(v1,v2)
        for v1,v2 in edges:
            res = -1
            for s1,n1 in g[v1]:
                if n1 in (v1,v2): continue
                for s2,n2 in g[v2]:
                    if n2 in (n1,v1,v2): continue
                    res = max(res, -s1-s2)
            if res != -1: msf = max(msf, res+sc[v1]+sc[v2])
        return msf
