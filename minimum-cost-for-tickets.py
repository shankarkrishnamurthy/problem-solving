from bisect import *
class Solution(object):
    def mincostTickets(self, days, c):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        l = len(days)
        cp=[0]*l
        def indx(d):
            i = bisect_left(days,d)
            if days[i] == d: return i
            else: return i-1
        def mct(n):
            if n < 0: return 0
            if cp[n] > 0: return cp[n]
            n1 = indx(days[n]-30)
            v1 = mct(n1) + c[2]

            n2 = indx(days[n]-7)
            v2 = mct(n2) + c[1]

            n3 = indx(days[n]-1)
            v3 = mct(n3) + c[0]

            cp[n] = min(v1,v2,v3)
            return cp[n]
        res = mct(l-1)
        return res
        
print Solution().mincostTickets([1,4,6,7,8,20], [2,7,15])
print Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
