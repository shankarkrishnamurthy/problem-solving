class Solution:
    def splitArray(self, nums, m):
        def sof(i,j): return nl[j] - nl[i] + nums[i] # sum of [i,j] inclusive
        @lru_cache(None)
        def walk(i, k):
            if n-i == k: return max(nums[i:])
            if k == 1: return sof(i, n-1)
            v = sys.maxsize
            for j in range(i+1, n-k+2):
                x = sof(i,j-1)
                if x > v: break
                v = min(v, max(x, walk(j, k-1)))
            return v
        n, nl = len(nums), [0]*len(nums)
        for i in range(n): nl[i] = nl[i-1] + nums[i]
        return walk(0, m)
