class Solution:
    def numSubmatrixSumTarget(self, mat, tgt):
        m, n, res = len(mat), len(mat[0]), 0
        for r in mat:
            for j in range(1,len(r)):
                r[j] += r[j-1]
        for i in range(n):
            for j in range(i,n):
                psh, s = defaultdict(int), 0
                psh[0] = 1
                for k in range(m):
                    s += mat[k][j] - (mat[k][i-1] if i > 0 else 0)
                    res += psh[s-tgt]
                    psh[s] += 1
                    #print(i,j, k,  dict(psh), 'res', res)
        return res
