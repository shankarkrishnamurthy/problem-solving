import numpy as np
class Solution(object):
    def maximalSquare(self, m):
        if not m: return 0
        r = len(m)
        c = len(m[0])
        mm, maxs = [[0 for y in range(c+1)] for x in range(r+1)],0
        for i in range(1,r+1):
            for j in range(1,c+1):
                if m[i-1][j-1] == '1':
                    minm = min(mm[i-1][j], mm[i-1][j-1], mm[i][j-1]) + 1
                    mm[i][j] = minm
                    maxs = max(maxs, minm)
        print np.array(mm)
        return maxs**2

    def maximalSquare2(self, matrix):
        R = len(matrix)
        C = len(matrix[0]) if R else 0
        memo, ml = [[0]*(C+1) for _ in range(R+1)], 0
        print np.array(memo)
        for r in range(1, R+1):
            for c in range(1, C+1):
                if matrix[r-1][c-1] == '1':
                    val = min(memo[r-1][c-1], memo[r][c-1], memo[r-1][c]) + 1
                    memo[r][c] = val
                    ml = max(ml, val)
        print np.array(memo)
        return ml*ml

print Solution().maximalSquare([])
print Solution().maximalSquare(["1"])
print Solution().maximalSquare(["0"])
print Solution().maximalSquare([["0"],["1"]])
print Solution().maximalSquare([["1","1"],["1","1"]])
print Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
