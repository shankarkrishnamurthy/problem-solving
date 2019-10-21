from typing import *
class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        if len(c) == 2: return True   
        h = True if c[1][0] == c[0][0] else False
        if not h:
            m = (c[1][1]-c[0][1])/(c[1][0]-c[0][0])
            x = c[0][1] - m*c[0][0]
        for i in range(2,len(c)):
            p = c[i]
            if h:
                if p[0] != c[0][0]: return False
            else:
                if p[1] != m*p[0] + x: return False
        return True

print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
print(Solution().checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))
