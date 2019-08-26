from random import *
from bisect import *
class MajorityChecker(object):
    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr = arr
        self.h = {}
        for i,v in enumerate(arr): self.h.setdefault(v,[]).append(i)
        

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        for i in xrange(20):
            k = self.arr[randint(left, right)]
            l = bisect_left(self.h[k], left)
            r = bisect_right(self.h[k], right)
            if r-l >= threshold: return k 
        return -1 


# Your MajorityChecker object will be instantiated and called as such:
obj = MajorityChecker([1,1,2,2,1,1])
print obj.query(0,5,4)
print obj.query(0,3,3)
print obj.query(2,3,2)
