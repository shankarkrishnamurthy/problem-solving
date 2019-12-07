from typing import *
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans,[px,py] = 0, points[0]
        for i in range(1, len(points)):
            x,y = points[i]
            a,b = abs(x-px),abs(y-py)
            ans += max(a,b)
            px,py = x,y
        return ans
        

print(Solution().minTimeToVisitAllPoints([[3,2]]))
print(Solution().minTimeToVisitAllPoints([[3,2],[-2,2]]))
print(Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
