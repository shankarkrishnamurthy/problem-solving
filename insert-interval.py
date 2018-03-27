# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def findInt(nI):
            si = -1
            sf = False
            for i,v in enumerate(intervals):
                if v.end < nI.start:
                    continue
                if v.start <= nI.start:
                    sf = True
                si = i
                break
            if si == -1: si = len(intervals)

            ei = -1
            ef = False
            for i,v in enumerate(intervals[si:]):
                if v.end < nI.end:
                    continue
                if v.start <= nI.end:
                    ef = True
                ei = i + si
                break
            if ei == -1: ei = len(intervals)

            return (sf,si,ef,ei)

        def pI(Inter):
            for i in Inter:
                print '[',i.start,',',i.end,']',
            print ''

        pI(intervals)
        if not intervals : return newInterval
        sf,si,ef,ei = findInt(newInterval)
        sv = intervals[si].start if sf else newInterval.start
        ev = intervals[ei].end if ef else newInterval.end
        if ef:
            ei += 1
        print sf,si,ef,ei, "sv", sv, "ev", ev,
        intervals[si:ei] = [Interval(sv,ev)]
        pI(intervals)
        return intervals


ni = Interval(2,5)
Solution().insert([], ni)
i1 = Interval(1,3)
i2 = Interval(6,9)
ni = Interval(2,5)
Solution().insert([i1,i2], ni)
i1 = Interval(1,2)
i2 = Interval(3,5)
i3 = Interval(6,7)
i4 = Interval(8,10)
i5 = Interval(12,16)
ni = Interval(4,9)
Solution().insert([i1,i2,i3,i4,i5], ni)
i1 = Interval(1,3)
ni = Interval(4,5)
Solution().insert([i1], ni)
i1 = Interval(3,4)
ni = Interval(1,2)
Solution().insert([i1], ni)
i1 = Interval(1,4)
ni = Interval(2,8)
Solution().insert([i1], ni)
i1 = Interval(7,9)
ni = Interval(2,8)
Solution().insert([i1], ni)
