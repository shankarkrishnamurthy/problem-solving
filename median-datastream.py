from heapq import heappush
from heapq import heappop
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxheap = [] # left side
        self.minheap = [] # right side
    def getFromMaxHeap(self):
            return -1*self.maxheap[0]

    def addNum(self, i):
        """
        :type num: int
        :rtype: void
        """
        def insertInMax(i):
            heappush(self.maxheap, -1*i)
        def popFromMaxHeap():
            return -1*heappop(self.maxheap)

        leftmax = rightmin = None
        if self.maxheap: leftmax = self.getFromMaxHeap()
        if self.minheap: rightmin = self.minheap[0]

        if leftmax or rightmin:
            if leftmax and i <= leftmax: insertInMax(i)
            else: heappush(self.minheap, i)
        else: heappush(self.minheap, i)

        l1 = len(self.minheap)
        l2 = len(self.maxheap)
        if abs(l1 -l2) > 1:
            if l1 > l2:
                e = heappop(self.minheap)
                insertInMax(e)
            else:
                e = popFromMaxHeap()
                heappush(self.minheap, e)
        print "min",self.minheap
        print "max",self.maxheap

    def findMedian(self):
        """
        :rtype: float
        """
        l1 = len(self.minheap)
        l2 = len(self.maxheap)
        if abs(l1-l2) > 0:
            median = self.minheap[0] if l1 > l2 else self.getFromMaxHeap()
        else:
            median = float(self.getFromMaxHeap() + self.minheap[0])/2.0
        return median

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(10)
print "Median",obj.findMedian()
obj.addNum(5)
print "Median",obj.findMedian()
obj.addNum(15)
print "Median",obj.findMedian()
obj.addNum(20)
print "Median",obj.findMedian()
obj.addNum(25)
print "Median",obj.findMedian()
