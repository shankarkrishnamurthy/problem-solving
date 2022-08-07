class Solution:
    def numberOfUniqueGoodSubsequences(self, b):
        dp0, dp1, f = 0, 0, 0
        for i in b:
            if i == '0': n0, n1, f = dp0 + dp1, dp1, 1
            else: n0, n1 = dp0, dp0 + dp1 + 1
            dp0, dp1 =n0, n1
        return (dp0 + dp1 + f) % (10**9+7)
