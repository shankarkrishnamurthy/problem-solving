class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lp = 0
        A.sort(reverse=True)
        n = len(A)
        #print A,n
        for i in range(0, n - 2): 
            if A[i] < (A[i + 1] + A[i + 2]): 
                lp = max(lp, A[i] + A[i + 1] + A[i + 2]) 
                break
        
        return lp

print Solution().largestPerimeter([3,6,2,3])
print Solution().largestPerimeter([3,2,3,4])
print Solution().largestPerimeter([1,2,1])
print Solution().largestPerimeter([2,1,2])
print Solution().largestPerimeter([4,1,2])
