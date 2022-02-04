class Solution:
    def trailingZeroes(self, n):
        s, c = 1, 0
        for i in range(1,n+1):
            s *= i
            while s % 10 == 0:
                s //= 10
                c += 1
            s = s % 10
        return c

print (Solution().trailingZeroes(5))
#print (Solution().trailingZeroes(100))
#print (Solution().trailingZeroes(1000))
