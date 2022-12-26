class Solution:
    def maximumTastiness(self, p, k):
        def check(m):
            c, prev = 1, 0
            for i in range(1, len(p)):
                if p[i] - p[prev] >= m:
                    c += 1
                    prev = i
                if c >=k: break
            return c>=k
        p.sort()
        l, r = 0, p[-1] - p[0] + 1
        while l < r:
            m = (l+r)//2
            if check(m): l = m+1
            else: r = m
        return l-1
