class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        def isleap(y):
            if y % 400 == 0: return True
            if y % 100 == 0: return False
            if y % 4 == 0: return True
            return False

        dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        nod = [31,28,31,30,31,30,31,31,30,31,30,31]
        soy = sum(nod)
        d = 0
        for i in xrange(1967,year): d += (soy+1 if isleap(i) else soy)
        for i in xrange(0,month-1): 
            d += nod[i]
            if i == 1 and isleap(year): d+=1
        d += day-1
        return dow[d % 7]
        
#print Solution().dayOfTheWeek(day = 1, month = 1, year = 1967)
print Solution().dayOfTheWeek(day = 21, month = 12, year = 1980)
#print Solution().dayOfTheWeek(day = 31, month = 8, year = 2019)
#print Solution().dayOfTheWeek(day = 18, month = 7, year = 1999)
#print Solution().dayOfTheWeek(day = 15, month = 8, year = 1993)
