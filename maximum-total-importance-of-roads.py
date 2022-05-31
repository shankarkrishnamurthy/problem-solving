class Solution:
    def maximumImportance(self, n, roads):
        g, c, res = [0]*n, 1, 0
        for (i,j) in roads:
            g[i] += 1
            g[j] += 1
        kl = sorted(enumerate(g), key=lambda x: x[1])
        #print(kl)
        for (i,v) in kl:
            #dp[i] = c
            res += g[i]*c
            c += 1
        #print(dp)
        return res
        
