class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        num,maxarea = len(points),0.0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    [x1,y1],[x2,y2],[x3,y3] = points[i],points[j],points[k]
                    ca =abs(.5*float(x1*y2+x2*y3+x3*y1-x1*y3-x3*y2-x2*y1))
                    print x1,y1,x2,y2,x3,y3,ca
                    maxarea = max(maxarea, ca)
        return maxarea

print Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
