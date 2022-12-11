class FenwickTree:
    def _update(o, i, v):
        while i < len(o.bit):
            o.bit[i] += v
            i += i & -i
    def _query(o, i):
        if i == 0: return 0
        s = 0
        while i:
            s += o.bit[i]
            i -= i & -i
        return s
    def __init__(o, n):o.bit = [0]*(n+1)
    def update(o, index, val): o._update(index+1, val)
    def query(o, index): return o._query(index+1)
class Solution:
    def maxPoints(self, g, qs):
        q, m, n = [(g[0][0], 0,0)], len(g), len(g[0])
        mn, vis, mns, res, ft = m*n, {}, set(), [], FenwickTree(1000002)
        while len(mns) < mn:
            while (q[0][1],q[0][2]) in mns: heappop(q)
            masf, i, j = heappop(q)
            mav = max(masf, g[i][j])
            mns.add((i,j))
            ft.update(mav+1, 1)
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if not (0<=x<m and 0<=y<n): continue
                if (x,y) not in vis or vis[(x,y)] > mav: 
                    heappush(q, (mav,x,y))
                    vis[(x,y)] = mav
        for q in qs: res.append(ft.query(q))
        return res
