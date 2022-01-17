class Solution:
    def combinationSum4(self, n, tgt):
        dp = [0]*(tgt+1)
        dp[0] = 1
        for i in range(tgt+1):
            for j in n:
                if i-j >= 0:
                    dp[i] += dp[i-j]
        return dp[tgt]

print(Solution().combinationSum4([1,2,3], 4))
print(Solution().combinationSum4([9], 3))
