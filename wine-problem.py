import numpy as np
class Solution(object):
    def maxwineprofit(self, prices):
        n = len(prices)
        dp = [[0]*n for _ in range(n)]
        print prices, n
        for sz in range(0,n):
            yr = n-sz
            for i in range(n-sz):
                en = i+sz
                if i == en:
                    dp[i][en] = yr*prices[i]
                    continue
                dp[i][en] = max(dp[i+1][en] + yr*prices[i], dp[i][en-1] + yr*prices[en])

        return dp[0][n-1]


print Solution().maxwineprofit([1,4,2,3])
print Solution().maxwineprofit([2,3,5,1,4])
