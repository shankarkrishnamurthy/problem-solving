class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        def isleap(y):
            if y % 400 == 0: return True
            if y % 100 == 0: return False
            if y % 4 == 0: return True
            return False

        da = [31,28,31,30,31,30,31,31,30,31,30,31]
        y,m,d = date.split('-')
        if (isleap(int(y))): da[1] = 29
        ans = 0
        for i in xrange(int(m)-1):
            ans += da[i]    
        ans += int(d)
        return ans

print Solution().dayOfYear("2004-03-01")
print Solution().dayOfYear("2003-03-01")
print Solution().dayOfYear("2019-02-10")
print Solution().dayOfYear("2019-01-09")
