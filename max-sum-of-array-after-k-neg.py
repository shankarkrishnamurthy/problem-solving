from bisect import *
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        i = bisect_left(A,0)
        if K <= i:
            for k in range(K):
                A[k] *= -1
        else:
            for k in range(i):
                A[k] *= -1
            K -= i
            A.sort()
            if K % 2 == 1:
                A[0] *= -1
        return sum(A)
                
        
        
print Solution().largestSumAfterKNegations([5,6,9,-3,3],2)
print Solution().largestSumAfterKNegations([4,2,3], 1)
print Solution().largestSumAfterKNegations([3,-1,0,2], 3)
print Solution().largestSumAfterKNegations([2,-3,-1,5,-4], 2)
