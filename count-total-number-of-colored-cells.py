class Solution:
    def coloredCells(self, n: int) -> int:
        res, d = 1, 4
        for i in range(n-1):
            res += d
            d += 4
        return res
