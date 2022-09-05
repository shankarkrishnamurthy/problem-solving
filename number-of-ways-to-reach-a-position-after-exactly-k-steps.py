class Solution:
    def numberOfWays(self, sp, ep, k):
        P=defaultdict(int)
        P[sp], m = 1, 1000_000_007
        for i in range(1,k+1):
            th = defaultdict(int)
            for p in P:
                th[p-1], th[p+1] = (th[p-1]+P[p]) % m, (th[p+1]+P[p]) % m
            P = th
        #print('P', dict(P))
        return P[ep]
