import numpy as np
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        As,Bs = set(A),set(B)
        a = [i for i in A if i in Bs]
        b = [i for i in B if i in As]
        m,n = len(a), len(b)
        if not m or not n: return 0
        #print a,b
        dp = [[0 for _ in range(n)] for i in range(m)]
        for i in xrange(m):
            for j in xrange(n):
                if a[i] == b[j]: 
                    dp[i][j] = 1 + (dp[i-1][j-1] if i>0 and j >0 else 0)
                else:
                    dp[i][j] = max(dp[i-1][j] if i > 0 else 0, dp[i][j-1] if j > 0 else 0)
        #print np.array(dp)
        return dp[m-1][n-1]
        

print Solution().maxUncrossedLines([1], [4])
print Solution().maxUncrossedLines([1,4,2], [1,2,4])
print Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2])
print Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1])
print Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,7,5,1])
