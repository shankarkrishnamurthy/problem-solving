class Solution:
    def countGood(self, nums, k):
        res, l, tp, hv = 0, 0, 0, defaultdict(int)
        for i,v  in enumerate(nums):
            hv[v] += 1
            tp += hv[v] - 1
            #print((i,v), 'tp ', tp)
            while tp >= k:
                lv, l = nums[l], l+1
                hv[lv] -= 1
                tp -= hv[lv]
            res += l
        return res
