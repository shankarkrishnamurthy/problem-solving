class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        if N==3: return 6
        if N<4: return N
        while N > 3:
            x = N*(N-1)/(N-2)
            if ans == 0: 
                ans = x
                x = 0
            ans += N-3 - x
            N -= 4
        if N==3: return ans-3*2/1
        elif N==2: return ans-2*1
        elif N==1: return ans-1
        else: return ans
        
print Solution().clumsy(10000)
print Solution().clumsy(4)
print Solution().clumsy(8)
print Solution().clumsy(9)
print Solution().clumsy(10)
print Solution().clumsy(11)
