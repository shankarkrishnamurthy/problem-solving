class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lm,i,cl = 0,1,-1
        if len(A) < 3: return 0
        print A
        while i < len(A)-1:
            if A[i] > A[i-1] and A[i] > A[i+1]:
                # Found a mountain peak
                r = i + 1
                while r < len(A)-1 and A[r] > A[r+1]: 
                    r += 1
                if lm < r - cl : 
                    lm = r-cl
                i = r
                print "new mountain ",cl,r, lm
                cl = r-1
            else: 
                if A[i-1] >= A[i]: cl = i-1
                i += 1
        return lm
        
print Solution().longestMountain([2,1,4,7,3,2,5])
print Solution().longestMountain([0,3,2,1,4,7,3,2,5])
print Solution().longestMountain([2,2,2])
print Solution().longestMountain([2,4,2])
