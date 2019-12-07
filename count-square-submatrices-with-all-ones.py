from typing import *
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1],dp[i+1][j]) + 1
        return sum([sum(_) for _ in dp])

print(Solution().countSquares([ [0,1,1,1], [1,1,1,1], [0,1,1,1] ]))
print(Solution().countSquares([ [1,0,1], [1,1,0], [1,1,0] ]))
