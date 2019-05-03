class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        pma = A[0] + 0
        msf = 0
        for j in range(1,len(A)):
            msf = max(pma + A[j]-j, msf)
            cva = A[j] + j
            pma = cva if cva > pma else pma
        return msf
            
        
print Solution().maxScoreSightseeingPair([8,1,5,2,6])
