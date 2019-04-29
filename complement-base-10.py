class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        for i in range(1,31):
            if N < 2**i: break
        return (2**i)-1-N
        
print Solution().bitwiseComplement(5)
print Solution().bitwiseComplement(7)
print Solution().bitwiseComplement(10)
print Solution().bitwiseComplement(8)
print Solution().bitwiseComplement(0)
print Solution().bitwiseComplement(10**9)
