from math import *
class Solution:
    def abbreviateProduct(self, l, r):
        p, s, c, fc = 0, 1, 0, 0
        for i in range(l,r+1):
            s *= i
            while s % 10 == 0: 
                s//=10
                c += 1
            if not fc: 
                if len(str(s)) > 10: fc = 1
            s = s % 10**11
            p += log10(i)

        p = p - int(p)
        p = (10**6)*pow(10,p)
        print(p,s)
        if fc:
            return str(p)[:5] + '...' + str(s)[-5:] + 'e' + str(c)
        else:
            return str(s) + 'e' + str(c)
        

print(Solution().abbreviateProduct(3,18))
#print(Solution().abbreviateProduct(40,40))
#print(Solution().abbreviateProduct(1,4))
#print(Solution().abbreviateProduct(2,11))
#print(Solution().abbreviateProduct(999998,1000000))
#print(Solution().abbreviateProduct(2,80))
