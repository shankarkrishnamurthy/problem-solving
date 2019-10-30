from typing import *
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        s = [0,1]
        for i in range(1,n):
            s += [s[k]|1<<i for k in range(len(s)-1,-1,-1)]
            
        s += s
        p = s.index(start)
        return s[p:p+2**n] 
        

print(Solution().circularPermutation(1,0))
print(Solution().circularPermutation(1,1))
print(Solution().circularPermutation(2,3))
print(Solution().circularPermutation(3,2))
print(Solution().circularPermutation(5,17))
