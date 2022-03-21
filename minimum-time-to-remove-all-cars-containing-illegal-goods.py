class Solution:
    def minimumTime(self, s):
        lsf, res, n = 0, len(s), len(s)
        for i,v in enumerate(s):
            lsf = min(lsf + 2*(v=="1"), i+1)
            res = min(res, lsf + n-i-1)
        return res
