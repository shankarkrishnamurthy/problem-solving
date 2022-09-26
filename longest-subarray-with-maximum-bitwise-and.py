class Solution:
    def longestSubarray(self, nums):
        v, res, l = max(nums), 1, -1
        for i in range(len(nums)):
            if nums[i]!=v: l = i
            else: res = max(res, i-l)
        return res
