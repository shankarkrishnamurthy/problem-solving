from bisect import *
class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        for l in range(n - 2, -1, -1):
            if A[l] > A[l + 1]:
                break
        else:
            return A
        r = A.index(max(a for a in A[l + 1:] if a < A[l]), l)
        A[l], A[r] = A[r], A[l]
        return A

print Solution().prevPermOpt1([3,2,1])
print Solution().prevPermOpt1([1,1,5])
print Solution().prevPermOpt1([1,9,4,6,7])
print Solution().prevPermOpt1([3,1,1,3])
print Solution().prevPermOpt1([3,1])
print Solution().prevPermOpt1([1,3])
print Solution().prevPermOpt1([3])
print Solution().prevPermOpt1([1,1,9,4,9,7,7,5,3,10,4,10,2,3,4,9,4,6,5,10,7,2,9,4,10,7,10,5,10,9,5,3,6,9,3,1,2,9,1,4,5,1,3,2,10,7,9,6,9,6,9,9,1,8,7,8,9,5,9,8,6,1,10,9])
