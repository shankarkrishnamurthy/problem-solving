class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        #print '\nA ', A
        F,n = [], len(A)
        for i in range(0,n-K+1):
            if i == 0:
                if A[i] == 0: F.append(1)
                else: F.append(0)
                continue
            m = F[i-1] - (F[i-K] if i >=K else 0)
            if (m % 2 == 0 and A[i] == 0) or (m % 2 == 1 and A[i] == 1):
                F.append(1 + F[i-1]) # one more flip
            else:
                F.append(F[i-1])
            #print i, A[i], m, 'Flips ', F
        #print 'Flips done ', F
        lf = F[-1]
        for i in range(n-K+1,n):
            m = F[i-1] - (F[i-K] if i >=K else 0)
            #print i, A[i], m, 'Flips ', F
            if (m % 2 == 0 and A[i] == 0) or (m % 2 == 1 and A[i] == 1): return -1
            F.append(F[i-1])
            
        return lf
            
print Solution().minKBitFlips([0,0,0], 3)
print Solution().minKBitFlips([1,1,1], 3)
print Solution().minKBitFlips([0,1,0], 1)
print Solution().minKBitFlips([1,1,0], 2)
print Solution().minKBitFlips([0,0,0,1,0,1,1,0], 3)
