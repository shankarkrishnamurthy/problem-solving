class Solution:
    def closestMeetingNode(self, el, n1, n2):
        t, dp, c = n1, [(-1,-1)]*len(el), 0, 
        while t!=-1 and dp[t][0] == -1: 
            dp[t], t, c = (0,c), el[t], c+1
        t, c, res, d = n2, 0, -1, sys.maxsize
        while t!=-1 and dp[t][0]!=1:
            if dp[t][0] == 0:
                if max(c, dp[t][1]) < d: res, d = t, max(c, dp[t][1])
                elif max(c, dp[t][1]) == d: res = min(res, t)
                dp[t] = (1, -1)
            else: dp[t] = (1,c)
            t, c = el[t], c+1
        return res
