class Solution:
    def maxTrailingZeros(self, g):
        def add(i,j,cur):
            t1,t2,f1,f2 = 0,0,0,0
            if i > 0:  t1,f1 = dp[i-1][j][0]
            if j > 0:  t2,f2 = dp[i][j-1][1]
            dp[i][j]= [(t1+cur[0],f1+cur[1]), (t2+cur[0],f2+cur[1])]
        def sub(dr, a,b,c,d):
            if dr == 'h':
                t1,f1 = dp[c][d][1]
                if b > 0: t2,f2 = dp[a][b-1][1]; t1,f1 = t1-t2,f1-f2
            else: 
                t1,f1 = dp[c][d][0]
                if a > 0: t2,f2 = dp[a-1][b][0]; t1,f1 = t1-t2,f1-f2
            return (t1,f1)
        def comb(e,f): return min(e[0]+f[0], e[1]+f[1])
        m,n, res = len(g), len(g[0]), 0
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                for t in range(1,11):
                    if g[i][j] % 2**t != 0: break
                for f in range(1,6):
                    if g[i][j] % (5**f) != 0: break
                add(i,j, (t-1,f-1))
        for i in range(m):
            for j in range(n):
                ltc, rtc, lbc, rbc = 0,0,0,0
                if i >= 0: ltc = comb(sub('v',0,j,i,j) , (sub('h',i,0,i,j-1) if j > 0 else (0,0)))
                if i >= 0: rtc = comb(sub('v',0,j,i,j), (sub('h',i,j+1,i,n-1) if j < n-1 else  (0,0)))
                if i <= m-1: lbc = comb((sub('h',i,0,i,j-1) if j > 0 else  (0,0)) , sub('v',i,j, m-1,j))
                if i <= m-1: rbc = comb(sub('v',i,j, m-1,j) , (sub('h', i,j+1, i,n-1) if j < n-1 else  (0,0)))
                res = max(res, ltc,rtc,lbc,rbc)
        return res
