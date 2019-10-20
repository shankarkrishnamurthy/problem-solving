import math
from bisect import  *
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        pn = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        np = bisect(pn,n)
        c = n - np 
        a = math.factorial(np) % ( 10**9 + 7)
        b = math.factorial(c) % ( 10**9 + 7)
        res = a*b  % ( 10**9 + 7)
        return res

print Solution().numPrimeArrangements(5)
print Solution().numPrimeArrangements(1)
print Solution().numPrimeArrangements(100)
print Solution().numPrimeArrangements(2)
print Solution().numPrimeArrangements(3)
