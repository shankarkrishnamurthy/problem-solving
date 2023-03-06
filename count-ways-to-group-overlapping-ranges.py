class Solution:
    def countWays(self, ranges):
        ranges.sort()
        print(ranges)
        ma, res = ranges[0][1], 2
        for i in range(1, len(ranges)):
            a,b = ranges[i]
            if a > ma:
                ma = b
                res *= 2
                res %= 1000000007
            else: ma = max(ma, b)
        return res
