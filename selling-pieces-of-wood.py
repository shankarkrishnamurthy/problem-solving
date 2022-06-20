class Solution:
    def sellingWood(self, m, n, pr):
        @lru_cache(None)
        def f(h,l):
            ans = mp[(h,l)]
            for i in range(1, 1+h//2):
                ans = max(ans, f(i, l) + f(h-i,l))
            for j in range(1, 1+l//2):
                ans = max(ans, f(h, j) + f(h,l-j))
            return ans
        
        mp = defaultdict(int)
        for (h,l,p) in pr: mp[(h,l)] = p
        return f(m,n)
