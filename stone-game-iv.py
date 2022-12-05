class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[-1]*(n+1)
        dp[0], dp[1]=0, 1
        for i in range(2,n+1):
            j = 1
            while j*j <= i:
                if dp[i-j*j] == 0:
                    dp[i] = 1
                    break
                j += 1
            if dp[i] == -1: dp[i] = 0
        return dp[n]
