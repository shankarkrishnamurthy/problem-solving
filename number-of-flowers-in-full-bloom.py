class Solution:
    def fullBloomFlowers(self, fl, pl):
        ll, res, bl = [], [0]*len(pl), 0
        for s,e in fl:
            ll.append((s,0, None))
            ll.append((e,2, None))
        for i,v in enumerate(pl):
            ll.append((v, 1, i))
        ll.sort()
        for t,c,i in ll:
            if c == 0: bl += 1
            elif c == 1: res[i] = bl
            else: bl -= 1
        return res
