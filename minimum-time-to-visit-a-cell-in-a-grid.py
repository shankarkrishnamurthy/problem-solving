class Solution:
    def minimumTime(self, g):
        m, n = len(g), len(g[0])
        if g[1][0] > 1 and g[0][1] > 1: return -1
        vis, q = defaultdict(int), [(0,0,0)]
        while q:
            v, x, y = heappop(q)
            if (x,y)==(m-1,n-1): return v
            for a,b in [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]:
                if (not 0<=a<m) or (not 0<=b<n): continue
                d = v + 1
                if g[a][b] > v+1:
                    d = g[a][b]+1 if (g[a][b] - v) % 2 == 0 else g[a][b]
                if (a,b) not in vis or vis[(a,b)] > d:
                    vis[(a,b)] = d
                    heappush(q, (d,a,b))

