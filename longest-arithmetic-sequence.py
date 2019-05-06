class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lh,msf=[{}],0
        for i in xrange(1,len(A)):
            cd = A[i] - A[i-1]
            h = {}
            h[cd] = h.get(cd,0) + 1
            msf = max(msf, h[cd])
            for j in range(i):
                ad = A[i] - A[j]
                h[ad] = lh[j][ad]+1 if ad in lh[j] else 1
                msf = max(msf, h[ad])
            lh.append(h)
        #print lh, msf+1
        return msf+1

print Solution().longestArithSeqLength([3,6,9,12])
print Solution().longestArithSeqLength([9,4,7,2,10])
print Solution().longestArithSeqLength([20,1,15,3,10,5,8])
print Solution().longestArithSeqLength([3,6,9,15,21,18])
