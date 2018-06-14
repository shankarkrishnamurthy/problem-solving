# Let dp[i] be probability of reaching exactly ith point
class Solution(object):
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W: return 1.0;
        dp = [1.0] + [0.0]*N
        PSumOfW = 1.0
        for i in range(1,N+1):
            dp[i] = PSumOfW/W
            if i < K: PSumOfW += dp[i]
            if i-W >= 0: PSumOfW -= dp[i-W]
        #print dp
        return sum(dp[K:])

print Solution().new21Game(55,50,10)
#print Solution().new21Game(21,17,10)
#print Solution().new21Game(6,1,10)
#print Solution().new21Game(2,2,2)
