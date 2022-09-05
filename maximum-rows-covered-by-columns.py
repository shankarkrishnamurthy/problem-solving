class Solution:
    def maximumRows(self, mat, col):
        def c1(n):
            c = 0
            while n: n, c = n & (n-1), c+1
            return c
        m, n, rl, res = len(mat), len(mat[0]), [], 0
        for r in mat: rl.append(int(''.join(map(str, r)) ,2))
        for i in range(2**n):
            cn, ccr = c1(i), 0
            if cn != col: continue
            for r in rl:
                if (r | i) == i: ccr += 1
            res = max(ccr, res)
        return res
                
        
