class Solution:
    def distinctSequences(self, n: int) -> int:
            if n < 2: return 6
            P, mod = {1: {2, 3, 4, 5, 6}, 2: {1, 3, 5}, 3: {1, 2, 4, 5}, 4: {1, 3, 5}, 5: {1, 2, 3, 4, 6}, 6: {1, 5}}, 1000000007
            prev = [[0] * 7 for _ in range(7)]
            for i in range(1, 7):
                for j in P[i]: prev[i][j] = 1
            for _ in range(n - 2):
                curr = [[0] * 7 for _ in range(7)]
                for i in range(1, 7):
                    for j in P[i]:
                        for k in range(1, 7):
                            if k != j:
                                curr[i][j] = (curr[i][j] + prev[k][i]) % mod
                prev = curr[:]
            return sum(sum(x) for x in prev) % mod
        
