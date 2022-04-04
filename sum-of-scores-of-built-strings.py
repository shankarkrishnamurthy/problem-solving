class Solution:
    def sumScores(self, s):
        def z_function(s):
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
                #print('i ', i, 'z ', z, 'l ', l, 'r ', r)
            return z
        n, z=len(s), [0] * len(s)
        return sum(z_function(s)) + n
