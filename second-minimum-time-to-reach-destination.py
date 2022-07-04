from heapq import *
class Solution:
    def secondMinimum(self, n, edges, ti, ch):
        g, hq, nt1, nt2=defaultdict(list), [], [float("inf")]*(n+1), [float("inf")]*(n+1)
        for (i,j) in edges: g[i].append(j), g[j].append(i)
        hq, cc, nct, res = [(0, 1), (ch, -1)], 1, ch, 0
        while hq:
            t, e = heappop(hq)
            #print('pop', (t,e), 'color', cc, 'res', res)
            if e == -1:
                nct, cc = t+ch, not cc
                heappush(hq, (nct, -1))
                continue
            if e == n:
                if not res: res = t
                elif res == t: pass
                else: return t
            for ne in g[e]:
                if not cc: mt = max(nct, t)
                else: mt = t
                if mt+ti == nt1[ne] or mt+ti == nt2[ne]: continue
                if mt+ti < nt1[ne]: nt1[ne], nt2[ne] = mt+ti, nt1[ne]
                elif mt+ti < nt2[ne]: nt2[ne] = mt+ti
                else: continue
                heappush(hq, (mt+ti, ne))
