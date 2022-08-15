class Solution:
    def maxValue(self, el, k):
        el.sort()
        n = len(el)
        @lru_cache(None)
        def dfs(i, k):
            if i == n or k == 0: return 0
            ni = bisect_left(el, [el[i][1]+1])
            res = max(dfs(i+1, k), dfs(ni, k-1) + el[i][2])        
            return res
        return dfs(0, k)
        
