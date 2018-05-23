import numpy as np
class Solution(object):
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[(0,0)]*n for _ in range(n)]
        #print nums, n
        for sz in range(0,n):
            for i in range(n-sz):
                en = i+sz
                if i == en:
                    dp[i][en] = (nums[i],0)
                    continue
                if dp[i+1][en][1] + nums[i] > dp[i][en-1][1] + nums[en]:
                    p1 = dp[i+1][en][1] + nums[i]
                    p2 = dp[i+1][en][0]
                else:
                    p1 = dp[i][en-1][1] + nums[en]
                    p2 = dp[i][en-1][0]

                dp[i][en] = (p1,p2)
        #print dp
        return dp[0][n-1][0] >= dp[0][n-1][1]

print Solution().PredictTheWinner([1,5,2])
print Solution().PredictTheWinner([1,4,2,3])
print Solution().PredictTheWinner([2,3,5,1,4])
