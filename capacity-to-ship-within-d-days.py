from bisect import *
class Solution(object):
    def shipWithinDays(self, w, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def numdays(n):
            d,i,t = 0,0,n
            while i < len(cw):
                i = bisect_left(cw, t)
                d += 1
                if i < len(cw):
                    if cw[i] == t: i+=1
                    t = cw[i-1] + n 
                #print '     ', 'day ', d, ' find ', t, ' index ', i 
            return d
        def accumulate(w):
            c,cw = 0, []
            for i in w:
                c += i
                cw.append(c)
            return cw

        l,r = max(w),sum(w)
        cw = accumulate(w)
        #print w,cw
        while l < r:
            m = (l + r)/2
            d = numdays(m)
            #print 'm ', m, 'days ', d, 'l ', l,  'r ',r
            if d > D:
                l = m + 1
            else:
                r = m
        return l
        
print Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)
print Solution().shipWithinDays([3,2,2,4,1,4], 3)
print Solution().shipWithinDays([1,2,3,1,1], 4)
