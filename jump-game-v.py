class Solution:
    def maxJumps(self, arr, d):
        @lru_cache(None)
        def check(i):
            mv1, st, en = 0, max(i-1, 0), max(i-d-1, -1)
            for k in range(st, en,-1):
                if arr[k] < arr[i]: 
                    mv1 = max(mv1, 1+check(k))
                else: break
            mv2, st, en = 0, min(len(arr)-1, i+1), min(len(arr), i+d+1)
            for k in range(st, en):
                if arr[k] < arr[i]:
                    mv2 = max(mv2, 1+check(k))
                else: break
            return max(mv1,mv2)
        res = 0
        for i in range(len(arr)):
            res = max(res, 1+check(i))
        return res
