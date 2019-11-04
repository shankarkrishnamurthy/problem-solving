from typing import *
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy,yx,ans = 0,0,0
        for (i,j) in zip(s1,s2):
            xy += (i == 'x') and (j == 'y')
            yx += (i == 'y') and (j == 'x')
        ans += xy//2 + yx//2
        #print(xy,yx,ans)
        if xy % 2 == 1 and yx % 2 == 1: ans += 2
        elif xy % 2 ==0 and yx % 2 == 0: pass
        else: ans = -1
        return ans
        
print(Solution().minimumSwap(s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"))
print(Solution().minimumSwap(s1 = "xx", s2 = "xy"))
print(Solution().minimumSwap(s1 = "xy", s2 = "yx"))
print(Solution().minimumSwap(s1 = "xx", s2 = "yy"))
