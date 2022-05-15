from heapq import *
class Solution:
    def countPaths(self, n, roads):
        ways, g, dist = [0]*n, [[] for i in range(n)], [float("inf")]*n
        for u,v,t in roads:
            g[u].append((v,t)), g[v].append((u,t))
        q, ways[0], dist[0], mod= [(0,0)], 1, 0, 10**9 + 7
        while q:
            t, c = heappop(q)
            if t > dist[c]: continue
            for nc, nt in g[c]:
                if t + nt < dist[nc]:
                    dist[nc] = t+nt
                    ways[nc] = ways[c]
                    heappush(q, (nt+t, nc))
                elif t+nt == dist[nc]:
                    ways[nc] = (ways[nc] + ways[c]) % mod
        return ways[-1]
            
        
