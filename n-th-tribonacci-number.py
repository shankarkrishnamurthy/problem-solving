class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,c,v=0,1,1,2
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 1
        else:
            while v < n: 
                t = a + b + c
                a = b
                b = c
                c = t
                v += 1
        return t
        

print Solution().tribonacci(0)
print Solution().tribonacci(1)
print Solution().tribonacci(2)
print Solution().tribonacci(3)
print Solution().tribonacci(4)
print Solution().tribonacci(25)
