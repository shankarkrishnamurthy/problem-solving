class Solution:
    def numberOfWays(self, cor):
        pi, res= [], 1
        for i,v in enumerate(cor):
            if v == 'S': pi.append(i)
        if len(pi) % 2 == 1 or len(pi) == 0: return 0
        for i in range(2,len(pi),2):
            res *= (pi[i] - pi[i-1])
        return res % (10**9+7)
