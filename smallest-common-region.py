from typing import *
from collections import deque
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], r1: str, r2: str) -> str:
        r = {}
        for i in regions:
            for j in range(1,len(i)):
                r[i[j]] = i[0]
        l1,l2=[r1],[r2]
        while True:
            if r1 not in r : break
            r1 = r[r1]
            l1.append(r1)
        while True:
            if r2 not in r: break
            r2 = r[r2]
            l2.append(r2)
        print(l1,l2)
        ans = l1.pop()
        l2.pop()
        while l1 and l2:
            a,b = l1.pop(),l2.pop()
            if a!=b: break
            ans = a
        return ans
    
    
print(Solution().findSmallestRegion(regions = [["Earth","North America","South America"], ["North America","United States","Canada"], ["United States","New York","Boston"], ["Canada","Ontario","Quebec"], ["South America","Brazil"]], r1 = "Quebec", r2 = "New York"))
print(Solution().findSmallestRegion([["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], "Canada", "Quebec"))
