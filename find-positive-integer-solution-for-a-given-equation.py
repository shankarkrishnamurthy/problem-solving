class cfunc1:
    def f(self,x,y): return x+y

class cfunc2:
    def f(self,x,y): return x*y

from typing import *
class Solution:
    def findSolution(self, cf: 'CustomFunction', z: int) -> List[List[int]]:
        l,r,ans = 1,1001,[]
        while r > 0 and l < 1001:
            c = cf.f(l,r)
            if z < c: 
                r-=1
            elif z == c:
                ans.append([l,r])
                l,r = l+1,r-1
            else:
                l+=1
        return ans

print(Solution().findSolution(cfunc1(),5))
print(Solution().findSolution(cfunc2(),5))
