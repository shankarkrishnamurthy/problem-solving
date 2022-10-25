class Solution:
    def maxBuilding(self, n, restr):
        dp, res= [], 0
        if not restr: return  n-1
        restr.sort()
        #print('restriction', restr)
        dp.append(min(restr[0][1], restr[0][0]-1))
        for i in range(1,len(restr)):
            dp.append(min(restr[i][1], dp[-1]+restr[i][0]-restr[i-1][0]))
        for i in range(len(restr)-2,-1,-1):
            dp[i] = min(dp[i], dp[i+1] + restr[i+1][0] - restr[i][0])
        #print('dp', dp)
        res = dp[0] + (restr[0][0]-1)//2
        for i in range(1,len(dp)):
            mh = max(dp[i],dp[i-1]) + (restr[i][0] - restr[i-1][0] - abs(dp[i] - dp[i-1]))//2
            res = max(res, mh)
            #print('max hgt', mh, 'b/w', i,'&',i-1, 'x', restr[i][0])
        if restr[-1][0] != n: res = max(res, dp[-1] + n - restr[-1][0])
        return res
