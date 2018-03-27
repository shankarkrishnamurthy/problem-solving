# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    @staticmethod
    def printInt(Int):
        for i in Int:
            print "(",i.start,",",i.end,")",
        print ""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals.sort(key=lambda x:x.start)
        res = [intervals[0]]
        for v in intervals[1:]:
            if v.start > res[-1].end: res.append(v)
            elif res[-1].end < v.end: res[-1].end = v.end
            #print  "(",v.start,",",v.end,")", "res",
            #Interval.printInt(res)
        return res

i1 = [Interval(8,17), Interval(15,18), Interval(1,3), Interval(2,6)]
Interval.printInt(Solution().merge(i1))
i1 = [Interval(1,2), Interval(2,3)]
Interval.printInt(Solution().merge(i1))
i1 = [Interval(1,2)]
Interval.printInt(Solution().merge(i1))

