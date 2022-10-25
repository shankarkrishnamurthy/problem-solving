class Solution:
    def longestNiceSubarray(self, nums):
        res, cor, l = 1, 0, 0
        for i,v  in enumerate(nums):
            while l < i and cor & v != 0:
                cor = cor & (~nums[l])
                l += 1
            cor = cor | v
            res = max(res, i-l+1)
        return res
        
