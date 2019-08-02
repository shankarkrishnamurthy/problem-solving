from bisect import *
class Solution(object):
    def largestValsFromLabels(self, v, l, num_wanted, use_limit):
        """
        :type v: List[int]
        :type l: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        h,ans = {},[]
        for a,b in zip(v,l):
            insort(h.setdefault(b,[]),a)
        for i in h:
            ans += h[i][-use_limit:]
        ans.sort(reverse=True)
        return sum(ans[:num_wanted])
        

print Solution().largestValsFromLabels([5,4,3,2,1], [1,1,2,2,3], 3, 1)
print Solution().largestValsFromLabels([5,4,3,2,1], [1,3,3,3,2], 3, 2)
print Solution().largestValsFromLabels([9,8,8,7,6], [0,0,0,1,1], 3, 1)
print Solution().largestValsFromLabels([9,8,8,7,6], [0,0,0,1,1], 3, 2)
