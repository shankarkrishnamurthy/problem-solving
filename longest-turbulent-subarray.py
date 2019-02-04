#!/bin/env python
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1: return 1
        r = [] # l = Ai < Ai-1, g Ai > Ai-1
        for i in range(1,len(A)):
            if A[i] < A[i-1]: r.append('l')
            elif A[i] > A[i-1]: r.append('g') 
            else: r.append('s')
        #print r
        msf,cs = 1,0
        for i,c in enumerate(r):
            if c == 's': cs = i+1
            elif c == 'l' and (i >0 and r[i-1] == 'l'): cs = i
            elif c == 'g' and (i>0 and r[i-1] == 'g'): cs = i
            else: pass
            mcur = (i+1) - cs + 1
            msf = max(mcur, msf)
        return msf
         
print Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9])
print Solution().maxTurbulenceSize([4,4,2,10,7,8,8,1,9])
print Solution().maxTurbulenceSize([1,4,2,10,7,8,8,1,9])
print Solution().maxTurbulenceSize([1,1,1])
print Solution().maxTurbulenceSize([1,1,1,2])
print Solution().maxTurbulenceSize([4,8,12,16])
print Solution().maxTurbulenceSize([100])
