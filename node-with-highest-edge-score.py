class Solution:
    def edgeScore(self, el):
        dp=[0]*len(el)
        for i, v in enumerate(el): dp[el[i]] += i
        #print(dp)
        mx = max(dp)
        return dp.index(mx)
