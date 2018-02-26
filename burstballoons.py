import numpy as np
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [x for x in nums if x>0]
        l = len(nums)
        if l == 0: return 0
        if l == 1: return nums[0]
        dp = [[0]*(l) for i in range(l)]
        nums.append(1)
        for sz in range(l):
            for st in range(l):
                en = st + sz
                if not en < l:
                    continue
                left = nums[st-1]
                right = nums[en+1]
                if st == en:
                    dp[st][en] = left * nums[st] * right
                    continue
                for k in range(sz+1):
                    st_k = st+k
                    lp = dp[st][st_k-1] if k > 0 else 0
                    rp = dp[st_k+1][en] if st_k < en else 0
                    previous = dp[st][en]
                    dp[st][en] = max(dp[st][en], lp + rp + nums[st_k]*left*right)
                    #print "st",st, "en",en,"k", k,"left",left,"right",right,"lp",lp,"rp",rp, "p", previous, "\tdp" , dp[st][en]
        return dp[0][l-1]
        
print Solution().maxCoins([0,0,0,0])
print Solution().maxCoins([0])
print Solution().maxCoins([8])
print Solution().maxCoins([8,3])
print Solution().maxCoins([1,1,1,1,1,1,1,1,1,1,1])
print Solution().maxCoins([2,2,2,2,2])
print Solution().maxCoins([3, 1, 5, 8])
