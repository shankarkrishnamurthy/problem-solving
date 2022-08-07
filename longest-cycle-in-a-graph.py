class Solution:
    def longestCycle(self, edges):
        dp, st, res=[(-1, -1)]*len(edges), 0, -1
        for i in range(len(edges)):
            if dp[i][0] != -1: continue # already visited
            st, t, c = st+1, i, 0
            while t!=-1 and dp[t][0] == -1:
                dp[t], t, c = (st, c), edges[t], c+1
            if t == -1: continue
            if dp[i][0] == dp[t][0]: 
                res = max(res, c - dp[t][1])
        return res
            
