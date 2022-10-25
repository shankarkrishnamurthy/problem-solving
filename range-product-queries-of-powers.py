class Solution:
    def productQueries(self, n, q):
        p, i, res = [], 0, []
        while n:
            if n & 1<<i: 
                p.append(i)
                n = n ^ (1<<i)
            i += 1
        for i in range(1,len(p)): p[i] += p[i-1]
        def psum(i,j): return p[j] - (p[i-1] if i > 0 else 0)
        for i,j in q:
            ps = psum(i,j)
            res.append((2**ps) % 1_000_000_007)
        return res
