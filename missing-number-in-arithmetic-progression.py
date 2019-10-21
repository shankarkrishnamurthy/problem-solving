from typing import *
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        s = []
        for i in range(1,len(arr)):
            v= arr[i]
            d = v - arr[i-1]
            if s and d!=s[-1]:
                if 2*s[-1]== d: return v-s[-1]
                else: return s[-2]-d
            elif not s: 
                s = [v,d]
                print (s)
            else: pass

print(Solution().missingNumber(arr = [5,7,11,13]))
print(Solution().missingNumber(arr = [15,13,12]))
print(Solution().missingNumber(arr = [1,2,3,5]))
print(Solution().missingNumber(arr = [80387,68178,55969,31551]))
