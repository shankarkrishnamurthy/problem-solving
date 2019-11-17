from typing import *
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            ln = arr[i-1] if i > 0 else float("inf")
            rn = arr[i+1] if i < len(arr)-1 else float("inf")
            res += arr[i]*min(ln,rn)
            del arr[i]
        return res

print(Solution().mctFromLeafValues([6,2,4]))
