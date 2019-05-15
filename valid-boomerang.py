class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x1,y1 = points[0]
        x2,y2 = points[1]
        x3,y3 = points[2]
        if len(set([tuple(i) for i in points])) != 3: return False
        if x1==x2==x3 or y1==y2==y3: return False
        m1 = float(x2-x1)/float(y2-y1) if y1 != y2 else float("Inf")
        m2 = float(x3-x2)/float(y3-y2) if y3 != y2 else float("Inf")
        print m1, m2
        return m1 != m2
            
        
print Solution().isBoomerang([[1,1],[2,3],[3,2]])
print Solution().isBoomerang([[1,1],[2,2],[3,3]])
print Solution().isBoomerang([[0,1],[0,1],[2,1]])
print Solution().isBoomerang([[0,1],[1,0],[1,1]])
print Solution().isBoomerang([[1,0],[0,0],[2,0]])
print Solution().isBoomerang([[80,32],[46,32],[59,32]])
print Solution().isBoomerang([[0,1],[1,0],[0,2]])
