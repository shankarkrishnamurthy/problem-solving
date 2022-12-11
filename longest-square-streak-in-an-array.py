class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res, cm, ns = 0, 0, set(nums)
        for i in ns:
            t, cm = i, 0
            while t in ns:
                t *= t
                cm += 1
            res = max(res, cm)
        if res < 2: return -1
        return res
