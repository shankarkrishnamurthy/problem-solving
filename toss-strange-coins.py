from typing import *
class Solution:
    def probabilityOfHeads(self,prob:List[float],t:int)->float:
        dp = {0: 1.0-prob[0], 1: prob[0]}
        for i in range(1,len(prob)):
            ph,pt,c =prob[i],1.0-prob[i],{}
            for i in range(min(len(dp),t+1)):
                if not i: c[0] = dp[0]*pt
                else: c[i] = dp[i-1]*ph + dp[i]*pt
            c[i+1] = dp[i]*ph
            dp = c
        print(dp)
        return round(dp[t],5)
            

print(Solution().probabilityOfHeads(prob=[0.4], t = 1))
print(Solution().probabilityOfHeads(prob=[0.5,0.5,0.5,0.5,0.5],t=0))
print(Solution().probabilityOfHeads(prob=[0.5, 0.3, 0.8, 0.15, 0.75], t= 4))
print(Solution().probabilityOfHeads(prob=[0.5, 0.3, 0.8, 0.15, 0.75], t= 2))
