from bisect import *
class Solution(object):
    def lastStoneWeight(self, s):
        """
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        i = len(s)-1
        while i>0:
            d = s[i] - s[i-1]
            s.pop()
            s.pop()
            #print i, s[i], s[i-1] ,s, 'af i', 
            if d > 0:
                insort(s,d)
                i -= 1
            else: i -= 2
            #print i
        if i < 0: return 0
        return s[0]

print Solution().lastStoneWeight([2,7,4,1,8,1])
print Solution().lastStoneWeight([2,7,4,1,8])
print Solution().lastStoneWeight([2,7])
print Solution().lastStoneWeight([7])
