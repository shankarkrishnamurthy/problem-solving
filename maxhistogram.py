class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        print heights,
        s = []
        maxarea, i, val = 0, 0, 0
        for i,v in enumerate(heights):
            if not s or (s and s[-1][1] < v):
                s.append((i,v))
                continue
            while s and s[-1][1] > v:
                (idx,val), span = s.pop(), i
                if s: span = i-s[-1][0]-1
                maxarea = max(maxarea, val*span)
            s.append((i,v))
        topidx = i+1
        while s:
            (idx,val), span = s.pop(), topidx
            if s: span = topidx - s[-1][0] - 1
            maxarea = max(maxarea, val*span)
        return maxarea

print Solution().largestRectangleArea([])
print Solution().largestRectangleArea([3])
print Solution().largestRectangleArea([9,5,3])
print Solution().largestRectangleArea([0,1,0,1])
print Solution().largestRectangleArea([1,2,1,2,1,2,1,2,1,2,1,2])
print Solution().largestRectangleArea([2,3,2,3,3,2,3,2,3,2,3])
print Solution().largestRectangleArea([2,5,6,8])
print Solution().largestRectangleArea([1,1,1,1])
print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([4,2,0,3,2,5])
print Solution().largestRectangleArea([3,6,5,7,4,8,1,0])
print Solution().largestRectangleArea([0,0,0,0,0,0,0,0,2147483647])

