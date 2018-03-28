class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sh = dict()
        if not nums: return 0
        msf = 1
        for v in nums:
            if sh.has_key(v):
                sh[v] += 1
                msf =max (msf, sh[v])
            else:
                sh[v] = 1
        return msf

print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
