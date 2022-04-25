class Solution:
    def countRectangles(self, rect, pt):
        hh, res = {}, [0]*len(pt)
        for l, h in rect:
            hh.setdefault(h, []).append(l)
        for i in hh: 
            hh[i].sort()
        hl = sorted(hh.keys())
        for i in range(len(pt)):
            l, h = pt[i]
            for j in range(bisect_left(hl, h), len(hl)):
                res[i] += len(hh[hl[j]]) - bisect_left(hh[hl[j]], l)
                #print((l,h), 'res', res)
        return res
