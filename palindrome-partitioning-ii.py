class Solution:
    def minCut(self, s):
        n, p= len(s), [[False]*len(s) for _ in range(len(s))]
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
        @lru_cache(None)
        def dfs(i):
            if i == n: return -1
            res = n
            for j in range(i+1, n+1):
                if not p[i][j-1]: continue
                res = min(res, 1+dfs(j))
            return res
        return dfs(0)
