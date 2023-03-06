class Solution:
    def waysToReachTarget(self, tgt, types):
        dp=[0]*(tgt+1)
        dp[0], MOD=1, 1000000007
        for c,m in types:
            ndp = list(dp)
            for t in range(m,tgt+1):
                for j in range(1,c+1):
                    if m*j <= t:
                        ndp[t] += dp[t-m*j] % MOD
                    else: break
            dp=ndp
        return dp[tgt] % MOD
