class Solution:
    def isBipartite(self, g):
        q, res, sc, vis = [0], [-1]*len(g), 'W', set() # bfs
        while q:
            nq = []
            for i in q:
                vis.add(i)
                if res[i] not in (-1, sc): return False
                res[i] = sc
                for j in g[i]:
                    if j not in vis: nq.append(j)
                
            if not nq: return True
            q = nq
            sc = 'B' if sc == 'W' else 'W'

print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))
print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print(Solution().isBipartite([[1],[0]]))
