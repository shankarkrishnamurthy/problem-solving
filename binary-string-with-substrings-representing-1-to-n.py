class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for i in xrange(N,N/2,-1):
            s = bin(i)[2:]
            if s not in S: return False
        return True
        
print Solution().queryString("0110", 3)
print Solution().queryString("0110", 4)
