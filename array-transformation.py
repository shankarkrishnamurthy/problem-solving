from typing import *
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        c,ch = arr,True
        while ch:
            p,ch = list(c), False
            for i in range(1,len(p)-1):
                if p[i] < p[i+1] and p[i] < p[i-1]:
                    ch = True
                    c[i] += 1
                elif p[i] > p[i+1] and p[i] > p[i-1]:
                    ch = True
                    c[i] -= 1
                else:
                    pass
        return c

print(Solution().transformArray(arr = [4]))
print(Solution().transformArray(arr = [6,4]))
print(Solution().transformArray(arr = [6,3,4]))
print(Solution().transformArray(arr = [6,9,4]))
print(Solution().transformArray(arr = [6,2,3,4]))
print(Solution().transformArray(arr = [1,6,3,4,3,5]))
