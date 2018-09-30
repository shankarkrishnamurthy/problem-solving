class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        msofar = A[0]
        lmax = A[0]
        lptr = 0
        for i in range(1,len(A)):
            if A[i] < lmax:
                lptr = i
                lmax = msofar
            else:
                msofar = max(msofar, A[i]) 
        return lptr+1

print Solution().partitionDisjoint([5,0,3,8,6])
print Solution().partitionDisjoint([1,1,1,0,6,12])
