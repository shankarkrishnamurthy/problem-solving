class Solution:
    def minimumTime(self, n, rel, ti):
        g, indeg = {i:set() for i in range(1,n+1)}, {i:0 for i in range(1,n+1)}
        q, msf,pt = [], 0, [0]*(n+1)
        for a,b in rel:
            g[a].add(b); indeg[b] += 1
        for i in indeg:
            if indeg[i] == 0: q.append((0,i))
        while q:
            nq = []
            for t, i in q:
                nt = t+ti[i-1]
                msf = max(msf, nt)
                for j in g[i]: # for each parent of 'i'
                    pt[j] = max(pt[j], nt)
                    indeg[j] -= 1
                    if indeg[j] == 0: nq.append((pt[j], j))
            if not nq: break
            q = nq
        return msf
