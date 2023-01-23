class Solution:
    def minCost(self, nums, k):
        @lru_cache(None)
        def walk(i):
            if i == n: return 0
            res, h, tr = math.inf, defaultdict(int), 0
            for j in range(i, n):
                h[nums[j]] += 1
                if h[nums[j]] != 1: 
                    if h[nums[j]] == 2: tr += 2
                    else: tr += 1
                res = min(res, k + tr + walk(j+1))
            return res
        n = len(nums)
        return walk(0)
