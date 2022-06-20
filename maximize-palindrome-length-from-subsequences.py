class Solution:
    def longestPalindrome(self, w1, w2):
        s, n, res = w1 + w2, len(w1), 0
        dp=[[-1]*len(s) for i in range(len(s))]
        def lps(i,j):
            nonlocal res
            if i > j: return 0
            if dp[i][j] != -1: return dp[i][j]
            if i == j:
                dp[i][j] = 1
                return 1
            if s[i] == s[j]: 
                sv = lps(i+1, j-1) + 2
                if i < n and j >= n: res = max(res, sv)
            else: sv = max(lps(i+1,j), lps(i,j-1))
            dp[i][j] = sv
            return sv
        lps(0, len(s)-1)
        return res
