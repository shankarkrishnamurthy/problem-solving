class Solution:
    def longestPalindromeSubseq(self, s):
        dp=[[-1]*len(s) for i in range(len(s))]
        def lps(i,j):
            if i > j: return 0
            if dp[i][j] != -1: return dp[i][j]
            if i == j:
                dp[i][j] = 1
                return 1
            if s[i] == s[j]: sv = lps(i+1, j-1) + 2
            else: sv = max(lps(i+1,j), lps(i,j-1))
            dp[i][j] = sv
            return dp[i][j]
        lps(0,len(s)-1)
        return dp[0][len(s)-1]
        
