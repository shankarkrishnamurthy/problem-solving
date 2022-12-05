class Solution:
    def maxPalindromes(self, s: str, x: int) -> int:
        n, p= len(s), [[False]*len(s) for _ in range(len(s))]
        if x == 1: return n
        for i in range(n):
            k = 0
            while 0<=i-k and i+k < n:
                if s[i-k] == s[i+k]: p[i-k][i+k] = True
                else: break
                k += 1
            if i >= n-1: continue
            k, j = 0, i+1
            while 0<=i-k and j+k < n:
                if s[i-k] == s[j+k]: p[i-k][j+k] = True
                else: break
                k += 1
        dp=[0]*n
        for i in range(x-1,n):
            for j in range(i-x+1, -1, -1):
                if p[j][i] == True:
                    dp[i] = max(dp[i], 1+ (dp[j-1] if j > 0 else 0))
                    break
            dp[i] = max(dp[i-1], dp[i])
        return dp[n-1]
