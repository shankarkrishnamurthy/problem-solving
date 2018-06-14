import numpy as np
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        def AVG(i,j):
            if i<=0 :
                return float(S[j])/(j+1)
            else:
                return float(S[j]-S[i-1])/(j-i+1)
            
        def lsoa(n,C):
            if L[n][C] != -1: return L[n][C]
            if C == 0: 
                L[n][C] = AVG(C,n)
                return L[n][C]
            maxavg = 0
            for i in range(C,n+1):
                if L[i-1][C-1] != -1:
                    v1 = L[i-1][C-1]
                else:
                    v1 = lsoa(i-1, C-1)
                v2 = AVG(i,n)
                if v1 + v2 > maxavg:
                    maxavg = v1 + v2
                    cut = i
            L[n][C] = maxavg
            return maxavg
        S,s,L = [],0,[[-1]*K for _ in range(len(A))]
        for v in A:
            s += v
            S.append(s)
        #print S
        a =  lsoa(len(A)-1,K-1)
        #print np.array(L)
        return a
        
print Solution().largestSumOfAverages([9,1,2,3,9],3)
