class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        dp,msf=[0]*n,-10**7
        for i in xrange(n):
            cma = -10**6
            for j in xrange(1,K+1):
                a = dp[i-j] if i-j >=0 else 0
                if i-j >= -1: 
                    cma = max(cma,A[i-j+1])
                    msf= max(msf,a + j*cma)
            dp[i] = msf
        #print dp
        return dp[n-1]

print Solution().maxSumAfterPartitioning([10,2], 2)
print Solution().maxSumAfterPartitioning([10], 1)
print Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)
