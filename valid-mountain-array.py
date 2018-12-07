class Solution(object):
    def validMountainArray(self, A):
        if len(A) < 3: return False
        peak = 0
        for i in range(1,len(A)-1):
            if A[i+1] < A[i] > A[i-1]:
                peak += 1
            if A[i] == A[i-1] or A[i] == A[i+1] or A[i-1] > A[i] < A[i+1]: return False
        return True if peak==1 else False

print Solution().validMountainArray([2,1])
print Solution().validMountainArray([3,5,5])
print Solution().validMountainArray([0,3,2,1])
print Solution().validMountainArray([1,2,3,4,5])
print Solution().validMountainArray([5,4,3])
print Solution().validMountainArray([0,1,2,1,2])
print Solution().validMountainArray([2,1,2,1,0])
                
