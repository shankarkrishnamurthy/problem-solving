class Solution:
    def minDistance(self, hl, k):
        n = len(hl)
        lms, rms= [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        def precalc():
            for i in range(n):
                cd = hl[i] - hl[i-1] if i > 0 else 0
                for j in range(i+1): lms[j][i] = (i - j)*cd + (lms[j][i-1] if i > 0 else 0)
            for i in range(n-1,-1,-1):
                cd = (hl[i+1] - hl[i]) if i < n-1 else 0
                for j in range(n-1,i-1,-1): rms[i][j] = (j-i)*cd + (rms[i+1][j] if i < n-1 else 0)
        @lru_cache(None)
        def totdist(i,j,k):
            if k == 1: return lms[i][(i+j)//2] + rms[(i+j)//2][j]
            res = sys.maxsize
            for x in range(i+1,j-k+3): res = min(res, totdist(i,x-1,1) + totdist(x, j, k-1))
            return res
        hl.sort(),precalc()
        return totdist(0,n-1, k)  
