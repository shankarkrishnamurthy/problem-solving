class Solution:
    def subStrHash(self, s, p, m, k, hv):
        n, res, ah, t = len(s), 0, {}, 1
        for i in range(26): ah[chr(ord('a')+i)] = i+1
        for i in range(n-k,n):
            v=ah[s[i]]
            res = (res + v*t) % m
            pre, t = t, t*p % m
        t = pre
        if res == hv: ans = n-k
        for i in range(n-k-1, -1,-1):
            ov, nv = ah[s[i+k]], ah[s[i]]
            res = ((res - ov*t)*p + nv) % m
            if res == hv: ans = i
        return s[ans:ans+k]
