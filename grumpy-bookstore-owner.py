class Solution(object):
    def maxSatisfied(self, c, g, X):
        """
        :type c: List[int]
        :type g: List[int]
        :type X: int
        :rtype: int
        """
        print c, g
        cum = [c[0] if not g[0] else 0]
        ncum = [c[0]]
        for i in xrange(1,len(c)):
            if g[i]: cum.append(cum[i-1])
            else: cum.append(cum[i-1]+c[i])
            ncum.append(ncum[i-1]+c[i])

        msf = ncum[X-1] + cum[-1]-cum[X-1]
        for i in xrange(X,len(c)):
            lx = ncum[i] - ncum[i-X]
            bef,aft = cum[i-X], cum[-1]-cum[i]
            print i,'lastx ', lx, 'bef ' ,bef, 'aft ', aft
            msf = max(msf, bef+lx+aft)
        print cum, ncum

        return msf
            

#print Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3)
print Solution().maxSatisfied([4,10,10],[1,1,0],2)
