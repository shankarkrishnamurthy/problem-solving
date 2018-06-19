class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1,len(A)-1):
            l,r = A[i-1], A[i+1]
            if A[i] > l and A[i] > r: 
                return i
            
            
        
print Solution().peakIndexInMountainArray([0,2,1,0])
print Solution().peakIndexInMountainArray([0,1,0])
