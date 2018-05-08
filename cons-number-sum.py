class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        count,i = 0, 1
        while( i * (i + 1) < 2 * N):
            a = (1.0*N - (i * (i + 1) ) / 2) / (i + 1)
            if a-int(a) == 0: count += 1
            i += 1
        return count+1

print Solution().consecutiveNumbersSum(15)
print Solution().consecutiveNumbersSum(9)
print Solution().consecutiveNumbersSum(5)
print Solution().consecutiveNumbersSum(832348)
#print Solution().consecutiveNumbersSum(697972)
