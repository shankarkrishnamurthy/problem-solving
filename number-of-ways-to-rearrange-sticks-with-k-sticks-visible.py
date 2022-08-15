class Solution:
    def rearrangeSticks(self, n, k):
        @lru_cache(None)
        def fn(n, k): 
            if n == k: return 1
            if k == 0: return 0
            return ((n-1)*fn(n-1, k) + fn(n-1, k-1)) % m
        m = 10**9+7
        return fn(n, k) 
