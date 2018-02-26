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
            #print "Adding: ", (i,v)
            if not s or (s and s[-1][1] < v):
                s.append((i,v,0))
                continue
            if s[-1][1] == v: continue
            while s and s[-1][1] > v:
                (idx,val,span) = s.pop()
                maxarea = max(maxarea, val*(i-idx+span))
                #print "  pop : ", (idx,val,span), " area", val*(i-idx+span)
            span += i-idx
            maxarea = max(maxarea, v*(span+1))
            s.append((i,v,span))
        topidx = i+1
        while s:
            (idx,val,span) = s.pop()
            maxarea = max(maxarea, val*(topidx-idx+span))
            #print "  pop : ", (idx,val,span), " area", val*(topidx-idx+span)
        if topidx:
            maxarea = max(maxarea, val*topidx)
        return maxarea

print Solution().largestRectangleArea([])
print Solution().largestRectangleArea([3])
print Solution().largestRectangleArea([2,3,6,8])
print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([9,5,3])
print Solution().largestRectangleArea([1,1,1,1])
print Solution().largestRectangleArea([4,2,0,3,2,5])
print Solution().largestRectangleArea([3,6,5,7,4,8,1,0])

