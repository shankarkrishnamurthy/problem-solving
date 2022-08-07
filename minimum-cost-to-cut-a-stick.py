class Solution:
    def minCost(self, n, cuts):
        @lru_cache(None)
        def docut(i, j):
            if j-i == 1: return 0
            res, cc= sys.maxsize, cuts[j] - cuts[i]
            for a in range(i+1, j):
                rc = docut(i, a) + docut(a,j) + cc
                res = min(res, rc)
            return res
        cuts = [0] + cuts + [n]
        cuts.sort()
        return docut(0, len(cuts)-1)
        
