class Solution(object):
    def trap(self, n):
        """
        :type height: List[int]
        :rtype: int
        """
        #print n
        s = []
        if len(n) < 3: return 0
        s.append((-1,n[0],0))
        wsf = 0
        for i,v in enumerate(n[1:]):
            cv = 0
            if v > s[-1][1]:
                while s and v > s[-1][1]:
                    idx,val,cval = s.pop()
                    cv += cval + val
                if not s:
                    wsf += val * (i-idx-1) - cv + val
                    cv = 0
            s.append((i,v,cv))
        
        while len(s) > 1:
            idx,val,cval = s.pop()
            wsf += (idx-s[-1][0]-1)*val - cval
        return wsf
        
print Solution().trap([3,1,2])
print Solution().trap([2,1,3])
print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print Solution().trap([1,1,1])
print Solution().trap([1,2,3,2,1])
print Solution().trap([1,2,3,4])
print Solution().trap([3,2,1,0])
print Solution().trap([0,3,2,1,0,1,2,1,3])
print Solution().trap([0,2,1,1,2,1,1,3])
print Solution().trap([2,1,3,1,1,2,1])
print Solution().trap([2,1,1,0,3])
