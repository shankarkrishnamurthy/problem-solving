class Solution:
    def minimumAverageDifference(self, nums):
        tot, rs, n, msf = sum(nums), 0, len(nums), 100001
        for i in range(n):
            rs += nums[i]
            os = tot - rs
            la, ra = rs // (i+1), (os // (n-i-1)) if i < n-1 else 0
            if msf > abs(la-ra):
                res, msf = i, abs(la-ra)
        return res
