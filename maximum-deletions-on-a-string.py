class Solution:
    def deleteString(self, s):
        n = len(s)
        @lru_cache(None)
        def dp(i):
            if i == n: return 0
            ans, j = 1, 1
            while i+2*j <= n and n-i-j+1 > ans:
                if s[i:i+j] == s[i+j:i+2*j]:
                    ans = max(ans, 1+dp(i+j))
                j += 1
            return ans
        return dp(0)
