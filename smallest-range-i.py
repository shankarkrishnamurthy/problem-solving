class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        minv = min(A)
        maxv = max(A)

        cdiff = maxv - minv
        maxvar = 2*K
        if cdiff <= 2*K: 
            return 0
        else: 
            return cdiff - 2*K

print Solution().smallestRangeI([1],0)
print Solution().smallestRangeI([0,10],2)
print Solution().smallestRangeI([1,3,6],3)
print Solution().smallestRangeI([0,3,9,5],3)
        
