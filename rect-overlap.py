class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1,y1,x2,y2 = rec1
        a1,b1,a2,b2 = rec2
        if x2 <= a1 or a2 <= x1 or y2 <= b1 or b2 <= y1: #rect up or down
            return False
        return True
        
print Solution().isRectangleOverlap([0,0,2,2],[1,1,3,3])
print Solution().isRectangleOverlap([0,0,1,1],[1,0,2,1])
