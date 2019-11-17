from typing import *
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2 ,l3, l4 = [], [], [], []
        for i in range(len(arr1)):
            l1 += [arr1[i]+arr2[i]+i]
            l2 += [arr1[i]-arr2[i]+i]
            l3 += [-arr1[i]+arr2[i]+i]
            l4 += [-arr1[i]-arr2[i]+i]
        return max(max(l1)-min(l1),max(l2) -min(l2),max(l3)-min(l3),max(l4)-min(l4))

print(Solution().maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))
print(Solution().maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6]))
