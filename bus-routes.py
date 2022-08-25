class Solution:
    def numBusesToDestination(self, routes, src, tgt):
        bsl, g = defaultdict(list), defaultdict(set)
        for b,r in enumerate(routes):
            for s in r:
                for pb in bsl[s]:
                    g[pb].add(b), g[b].add(pb)
                bsl[s].append(b)
        #print(dict(bsl),'\n', dict(g))
        res, q, dst, v = 1, bsl[src], set(bsl[tgt]), set(bsl[src])
        if not q or not dst: return -1
        while q:
            nq = []
            for bus in q:
                if bus in dst: return res
                for nbus in g[bus]:
                    if nbus in v: continue
                    v.add(nbus)
                    nq.append(nbus)
            if not nq: return -1
            q = nq
            res += 1    
        return res
