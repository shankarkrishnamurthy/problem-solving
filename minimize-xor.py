class Solution:
    def minimizeXor(self, num1, num2):
        def cnt(n):
            c = 0
            while n: n, c = n & (n-1), c+1
            return c
        n1, n2, res = cnt(num1), cnt(num2), num1
        #print(n1,n2)
        if n1 == n2: return res
        if n2 > n1:
            d, i = n2 - n1, -1
            while d:
                i += 1
                while (1<<i) & num1: i += 1
                res |= 1<<i
                d -= 1
        else: # n2 < n1
            d, i = n1 - n2, num1
            while d:
                i = i & (i-1)
                d -= 1
            res = i
        return res
