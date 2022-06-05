from bisect import *
class Solution:
    def partitionArray(self, nums, k):
        nums.sort()
        l, res = 0, 0
        while l < len(nums):
            res += 1
            r = bisect(nums, nums[l]+k)
            l = r
        return res
