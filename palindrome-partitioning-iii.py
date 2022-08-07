
class Solution:
    def palindromePartition(self, s, k):
        def calc():
            for i in range(n):
                l, r = i,i
                while 0<=l<n and 0<=r<n:
                    dp[l][r] = (dp[l+1][r-1] if l+1<=r-1 else 0)+(s[l]!=s[r])
                    l, r = l-1, r+1
                if i == n-1: continue
                l, r = i, i+1
                while 0<=l<n and 0<=r<n:
                    dp[l][r] = (dp[l+1][r-1] if l+1<=r-1 else 0)+(s[l]!=s[r])
                    l, r = l-1, r+1
        @lru_cache(None)
        def walk(st,k):
            if k==1: return dp[st][n-1]
            res = sys.maxsize
            for i in range(st+1, n-k+2): res = min(res, dp[st][i-1] + walk(i, k-1))
            return res
        s, n, dp = list(s), len(s), [[0]*len(s) for _ in range(len(s))]
        calc()
        return walk(0,k)
