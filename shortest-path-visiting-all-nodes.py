class Solution:
    def shortestPathLength(self, g):
        n, res = len(g), 0
        q, av = deque([(i, 1<<i) for i in range(n)]), (1<<n)-1
        vis=[set([1<<i]) for i in range(n)]
        while q:
            #print(q)
            ql = len(q)
            while ql:
                cn, cv = q.popleft()
                if cv == av: return res
                for nb in g[cn]:
                    nvis = cv | 1<<nb
                    if nvis == av: return res + 1
                    if nvis not in vis[nb]: 
                        vis[nb].add(nvis)
                        q.append((nb, nvis))
                ql -= 1
            res += 1
        return 0
