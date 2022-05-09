class Solution:
    def hasValidPath(self, g):
        def incr(pa):
            nonlocal mid
            for c in pa: 
                if 0 <= c+1 <= mid: npa[c+1] = npa.get(c+1, 0) + pa[c]
        def decr(pa):
            nonlocal mid
            for c in pa: 
                if 0 <= c-1 <= mid: npa[c-1] = npa.get(c-1, 0) + pa[c]
        def getcnt(i,j, c): return (c+1 if g[i][j] == '(' else c-1)
        m, n, c, c1 = len(g), len(g[0]), 0, 0
        dp, mid = [[{} for j in range(n)] for i in range(m)],  (m+n)//2
        for i in range(m): 
            c = getcnt(i, 0, c)
            if 0<=c<=mid: dp[i][0] = {c:1}
            else: break
        for j in range(n): 
            c1 = getcnt(0, j, c1)
            if 0<=c1<=mid: dp[0][j] = {c1:1}
            else: break
        for i in range(1,m):
            for j in range(1,n):
                upa, dpa, npa = dp[i-1][j], dp[i][j-1], {}
                if g[i][j] == '(': incr(upa), incr(dpa)  
                else: decr(upa), decr(dpa) 
                dp[i][j] = npa
        res = dp[m-1][n-1]
        return (0 in res and res[0] > 0)
