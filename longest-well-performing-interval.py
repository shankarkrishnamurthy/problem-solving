class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        sum, h,ml = 0, {},0
        for i,v in enumerate(hours):
            sum += (1 if v > 8 else -1)
            if sum not in h: h[sum] = i
            
            if sum > 0: ml = i + 1
            else:
                ml = max (ml, i - h.get(sum-1,i))
        return ml

print Solution().longestWPI([9,9,6,0,6,6,9])
print Solution().longestWPI([9,9,6,0,9,9])
