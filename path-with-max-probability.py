import heapq
import math
class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        g,v,sp={},set(),{}
        for i in range(n): g[i]=[]
        for i,(a,b) in enumerate(edges):
            g[a].append(b)
            g[b].append(a)
            sp[(a,b)]=succProb[i]
            sp[(b,a)]=succProb[i]
        q = [(0,start)]
        while q:
            #print(q)
            (p,e) = heapq.heappop(q)
            if e == end:
                return round(10**-p,6)
            v.add(e)
            for i in g[e]:
                if i in v: continue
                np = -p + math.log10(sp[(i,e)])
                heapq.heappush(q,(-np, i))
        return 0.0
            

print(Solution().maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))
print(Solution().maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))
print(Solution().maxProbability(3, [[0,1]], [0.5], 0, 2))
        
