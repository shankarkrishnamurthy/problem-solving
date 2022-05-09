class Solution:
    def countTexts(self, pk):
        dp, vv = [0]*(len(pk)+1), {2:3,3:3,4:3,5:3,6:3,7:4,8:3,9:4}
        dp[0], m = 1, 10**9 + 7
        for i,v in enumerate(pk):
            for j in range(vv[int(v)]):
                if v != pk[i-j] or i-j < 0: break
                dp[i+1] = ( dp[i+1] + dp[i-j] ) % m
        return dp[len(pk)]
