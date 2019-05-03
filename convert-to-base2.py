class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        print ' N ', N,
        if N==0: return '0'
        res,d,q,r= [], -2, N,0
        while q!=0:
            r = q % d
            if r < 0: r=-r
            pq = q
            q = q / d
            if q*d+r != pq: 
                q += 1
                #print 'check ',q, pq
            res.append(str(r))
            #print ' q ', pq, 'r ',r
        return ''.join(res[::-1])
def baseNeg2TOdec(s):
    val = 0
    for i,v in enumerate(s[::-1]):
        val += ((-2)**i)*int(v)
    return val
        
print Solution().baseNeg2(10**9)
print Solution().baseNeg2(1)
print Solution().baseNeg2(2)
print Solution().baseNeg2(18)
print Solution().baseNeg2(22)
print Solution().baseNeg2(0)
print Solution().baseNeg2(3)
print Solution().baseNeg2(4)
print Solution().baseNeg2(7)
print Solution().baseNeg2(8)
print Solution().baseNeg2(13)
