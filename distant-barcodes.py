from bisect import *
class Solution(object):
    def rearrangeBarcodes(self, bc):
        """
        :type bc: List[int]
        :rtype: List[int]
        """
        if len(bc)==1: return bc
        h={}
        for v in bc: h[v] = h.get(v,0)+1
        s_h = [(v,k) for k,v in h.items()]
        s_h.sort()
        res = []
        while len(s_h) > 1:
            #print s_h
            rc,rv=s_h.pop()
            lc,lv=s_h.pop()
            res += [rv,lv]*lc
            rc -= lc
            if rc: insort(s_h, (rc,rv))
        rc,rv = s_h[0] if s_h else (0,0)
        if rc: 
            res += [rv]
            i = res.index(rv)-1
            rc -= 1
        #print rc,rv
        for rc in xrange(rc,0,-1):
            #print len(res),'i ', i
            res.insert(i,rv)
            i -= 1
            
        #print len(res), len(bc)
        return res
                
print Solution().rearrangeBarcodes([1])
print Solution().rearrangeBarcodes([1,2])
print Solution().rearrangeBarcodes([1,2,1])
print Solution().rearrangeBarcodes([1,1,1,2,2,2])
print Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3])
print Solution().rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8])
print Solution().rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8,8])
print Solution().rearrangeBarcodes([51,83,51,40,51,40,51,40,83,40,83,83,51,40,40,51,51,51,40,40,40,83,51,51,40,51,51,40,40,51,51,40,51,51,51,40,83,40,40,83,51,51,51,40,40,40,51,51,83,83,40,51,51,40,40,40,51,40,83,40,83,40,83,40,51,51,40,51,51,51,51,40,51,83,51,83,51,51,40,51,40,51,40,51,40,40,51,51,51,40,51,83,51,51,51,40,51,51,40,40])
