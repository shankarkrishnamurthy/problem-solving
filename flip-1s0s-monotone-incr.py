class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        iarr,s1 = [],0
        for i in S:
            s1 += int(i)
            iarr.append(s1)
        msf = len(S)
        for i in range(len(S)+1):
            a = iarr[i-1] if i > 0 else 0
            b = iarr[-1] - (iarr[i-1] if i > 0 else 0)
            c = len(S) - i
            d = c - b
            cur = a + d
            msf = min(cur,msf)
            #print ' i ', i , ' cur ', cur , 'no. of 1 before ',a, ' no of 0 eq or after ',d
        return msf

print Solution().minFlipsMonoIncr("111") # 0 
print Solution().minFlipsMonoIncr("000") # 0
print Solution().minFlipsMonoIncr("00011000") # 2
print Solution().minFlipsMonoIncr("010110") # 2
print Solution().minFlipsMonoIncr("00110") # 1
