from operator  import mul
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        mall = 0
        for i in range(2,max(3,n/2)):
            q = n/i
            v = [q]*i
            for i in range(1,n%i+1):
                v[i-1] += 1
            now = reduce(mul, v, 1)
            if now < mall:
                break
            mall = now
        return mall
print Solution().integerBreak(2)
print Solution().integerBreak(3)
print Solution().integerBreak(5)
print Solution().integerBreak(10)
print Solution().integerBreak(25)
