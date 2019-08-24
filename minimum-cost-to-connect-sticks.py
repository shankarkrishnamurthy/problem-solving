from bisect import *
class Solution(object):
    def connectSticks(self, s):
        """
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        c = 0
        while len(s) > 1: 
            a,b = s.pop(0), s.pop(0)
            c += a+b
            insort(s,a+b)
        return c

print Solution().connectSticks([2,4,3])
print Solution().connectSticks([1,8,3,5])
