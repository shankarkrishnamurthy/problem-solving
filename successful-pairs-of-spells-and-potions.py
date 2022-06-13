from bisect import *
class Solution:
    def successfulPairs(self, sp, po, su):
        po.sort()
        res=[]
        for i,v in enumerate(sp):
            pv, m = divmod(su,v)
            if m==0: j = bisect_left(po, pv)
            else: j = bisect(po, pv)
            res.append(len(po) - j)
        return res
        
