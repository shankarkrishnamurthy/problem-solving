import math
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def fnt(val,dp):
            if val in dp: return dp[val]
            i,dpv = idx[val],0
            sqrt = math.sqrt(val)
            for j in range(i):
                p1 = A[j]
                if p1 <= sqrt and (val % p1) == 0:
                    p2 =val/A[j]
                    if p2 not in idx: continue
                    v1 = fnt(A[j],dp)
                    v2 = fnt(p2, dp)
                    print v1,v2
                    if A[j] == p2:
                        dpv += v1*v2
                    else:
                        dpv += v1*v2*2
            dp[val] = dpv+1
            return dp[val]
                
        n,res = len(A),0
        A.sort()
        idx = {v:i for i,v in enumerate(A)}
        dp = {}
        for i in range(n-1,-1,-1):
            fnt(A[i],dp)
            
        print ' dp ', dp
        return sum(dp.values()) % (10**9+7)

print( Solution().numFactoredBinaryTrees([45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48]))
#print( Solution().numFactoredBinaryTrees([2,3,4,6,9,12,18,36]))
#print( Solution().numFactoredBinaryTrees([18,6,3,2]))
#print Solution().numFactoredBinaryTrees([5,10,2,4,40])
#print Solution().numFactoredBinaryTrees([5,10,2,4])
#print Solution().numFactoredBinaryTrees([2,4])
