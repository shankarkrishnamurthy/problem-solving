from bisect import *
class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if X > Y : return X-Y
        o,n = [Y],Y
        while n > 1:
            n = (n+1)/2
            o.append(n)
        o = o[::-1]
        #print o, len(o)
        n = X
        i = bisect_left(o,n)
        res = 0
        while n < Y:
            print n, i, res
            if i > 0 and n != o[i]: i -= 1
            res += n - o[i]
            n = 2*o[i]
            res += 1
            i=bisect_left(o,n)
        if n > Y: res +=1
        return res
        

print Solution().brokenCalc(1,909999000)
print Solution().brokenCalc(2,3)
print Solution().brokenCalc(5,8)
print Solution().brokenCalc(3,10)
print Solution().brokenCalc(1024,1)
