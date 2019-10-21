from typing import *
from collections import deque
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = deque([[1,1,1,1,1,1,6]])
        for i in range(1,n):
            c = [0]*7
            for i,v in enumerate(rollMax):
                # seq ending in i+1
                for s in range(v):
                    if len(dp)-1 < s: 
                        c[i] += 1
                        break
                    c[i] += dp[s][6] - dp[s][i]
                c[6] += c[i]
                
            dp.appendleft(c)
            if len(dp) >16: dp.pop()

        return dp[0][6] % (10**9+7)
        
print(Solution().dieSimulator(2,[1,1,2,2,2,3]))
print(Solution().dieSimulator(2,[1,1,1,1,1,1]))
print(Solution().dieSimulator(3,[1,1,1,2,2,3]))
print(Solution().dieSimulator(4,[1,1,1,2,2,3]))
print(Solution().dieSimulator(20,[8,5,10,8,7,2]))
