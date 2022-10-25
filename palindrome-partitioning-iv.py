class Solution:
    def checkPartitioning(self, s):
        n, s = len(s), list(s)
        dp, l3 = [[False] * n for _ in range(n)], []
        for i in range(n-1, -1, -1):
            for j in range(max(0,i-1),n):
                if i >= j:
                    dp[i][j] = True
                    if j!=n-1 and dp[j+1][n-1]: l3.append(i)
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                    if dp[i][j] and j!=n-1 and dp[j+1][n-1]: l3.append(i)
        for i in l3:
            if i and dp[0][i-1]: return True
        return False
