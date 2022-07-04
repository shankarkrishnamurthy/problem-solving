class Solution:
    def countSpecialSubsequences(self, nums):
        z, o, t, m = 0, 0, 0, 7+10**9
        for i in nums:
            if i == 0: z = (2*z + 1) % m
            elif i == 1: o = (z + 2*o) % m
            else: t = (o + 2*t) % m
        return t
