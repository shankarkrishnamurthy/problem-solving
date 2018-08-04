class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = bin(N)
        prev, curr,msf = -1,-1,0
        for idx,i in enumerate(n[2:]):
            if i == '1': curr = idx
            if curr > -1 and prev > -1:
                msf = max(msf, curr - prev)
            prev = curr
        return msf
            

print Solution().binaryGap(1)
print Solution().binaryGap(6)
print Solution().binaryGap(22)
print Solution().binaryGap(5)
print Solution().binaryGap(8)
print Solution().binaryGap(10**8)
