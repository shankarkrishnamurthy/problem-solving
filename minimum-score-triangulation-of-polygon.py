import sys
class Solution(object):
    def minScoreTriangulation(self, A):
        #@lru_cache(None)
        dp = [[-1]*len(A) for _ in range(len(A))]
        def mst(i, j):
            if j - i + 1 < 3: return 0
            res = []
            if dp[i][j] != -1: return dp[i][j]
            for k in xrange(i+1,j):
                cv = A[i]*A[j]*A[k] + mst(i,k) + mst(k,j)
                res.append(cv)
            dp[i][j] = min(res)
            return dp[i][j]
        return mst(0, len(A) - 1)

print Solution().minScoreTriangulation([1,2,3])
print Solution().minScoreTriangulation([3,7,4,5])
print Solution().minScoreTriangulation([1,3,1,4,1,5])
