class Solution:
    def minCost(self, nums, cost):
        def getCost(avg):
            c = 0
            for i, v in enumerate(nums):
                c += cost[i]*abs(v - avg)
            return c
        l, r = min(nums), max(nums)
        if l == r: return getCost(l)
        while l < r:
            m = (l + r)//2
            mc = getCost(m)
            mp1c = (getCost(m+1) if m+1 <= r else float("inf"))
            if mc < mp1c: r = m
            else: l = m+1     
        return min(mc, mp1c)
