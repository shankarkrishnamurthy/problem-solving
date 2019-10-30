from typing import *
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a,b):
            if b == 0: return a
            return gcd(b, a%b)
        def lcm(a,b):
            return a*b//gcd(a,b)

        l , r = 1, min(a,b,c)*n
        #print('start ',r)
        if l == r: return n
        while l < r:
            mid = (l+r)//2
            na,nb,nc = mid//a,mid//b,mid//c
            nab,nbc,nca = mid//lcm(a,b),mid//lcm(b,c),mid//lcm(c,a)
            nabc = mid//lcm(lcm(a,b),c)
            z = na+nb+nc-nab-nbc-nca+nabc
            #print('mid ',mid,'l,r ',l,r, 'z ',z)
            if z == n: return mid-min(mid%a,mid%b,mid%c)
            if z < n:
                l = mid + 1
            else:
                r = mid
        return l
        
print(Solution().nthUglyNumber(n = 5, a = 2, b = 3, c = 3))
print(Solution().nthUglyNumber(n = 100000, a = 1, b = 3, c = 5))
print(Solution().nthUglyNumber(n = 3, a = 2, b = 3, c = 5))
print(Solution().nthUglyNumber(n = 4, a = 2, b = 3, c = 4))
print(Solution().nthUglyNumber(n = 5, a = 2, b = 11, c = 13))
print(Solution().nthUglyNumber(n = 1000000000, a = 2, b = 217983653, c = 336916467))
