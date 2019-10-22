from typing import *
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def maxSubArraySum(a): 
            #print(a)
            msf,meh = float("-inf")-1,0
            for i in range(0, len(a)): 
                meh = meh + a[i] 
                if (msf < meh): msf = meh 
                if meh < 0: meh = 0   
            return msf
        h0 = sum(arr)
        h1 = maxSubArraySum(arr)
        h2 = maxSubArraySum(arr+arr)
        #print('h0',h0,'h1',h1,'h2',h2,'k*h0',h0*k)
        if k < 3 or h0 < 0: return max(0,h0,h1,h2)

        return max(k*h0,h0*(k-2)+h2) % (10**9+7)

print(Solution().kConcatenationMaxSum(arr = [1,2], k = 3))
print(Solution().kConcatenationMaxSum(arr = [1,-2,1], k = 5))
print(Solution().kConcatenationMaxSum(arr = [-1,-2], k = 7))
print(Solution().kConcatenationMaxSum([-5,-2,0,0,3,9,-2,-5,4], 5))
