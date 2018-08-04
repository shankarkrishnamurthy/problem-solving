import math
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            if n % 2 == 0 and n > 2: 
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True
    
        def is_palin(n):
            s = str(n)
            sp = int(s[::-1])
            if n == sp: return True
            else: False
    
        print 'N ', N
        if N==1: return 2
        if is_palin(N) and is_prime(N): return N
        if N >= 9989900: N=10**8
        t = N+1 if N % 2 == 0 else N+2
        while True:
            #if is_prime(t) and is_palin(t): return t
            if is_palin(t): 
                if is_prime(t): return t
            t += 2

print Solution().primePalindrome(6)
print Solution().primePalindrome(8)
print Solution().primePalindrome(13)
print Solution().primePalindrome(10**8)
print Solution().primePalindrome(1003001)
print Solution().primePalindrome(1008001)
print Solution().primePalindrome(1022201)
print Solution().primePalindrome(1028201)
print Solution().primePalindrome(10543401)
print Solution().primePalindrome(10**7)
print Solution().primePalindrome(10**6)
print Solution().primePalindrome(10**5)
print Solution().primePalindrome(10**4)
print Solution().primePalindrome(10**3)
print Solution().primePalindrome(10**2)
print Solution().primePalindrome(10**1)
