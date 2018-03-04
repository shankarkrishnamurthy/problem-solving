class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L=0
        R=len(height)-1
        ma = 0
        while L < R:
            lh = height[L]
            rh = height[R]
            ma = max(ma, (R-L)*min(lh,rh))
            if lh < rh:
                L += 1
            else:
                R -= 1
        return ma
