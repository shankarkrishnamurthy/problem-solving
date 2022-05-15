class Solution:
    def waysToSplitArray(self, nums):
        tot, res, t = sum(nums), 0, 0
        for i in range(len(nums)-1):
            t += nums[i]
            res += int(t >= tot-t)
        return res
