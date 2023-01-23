class Solution:
    def minFlips(self, mat):
        res, m,n, q=0, len(mat), len(mat[0]), [[i[:] for i in mat]]
        z, vis=tuple([0]*m*n), set([tuple([j for i in mat for j in i])])
        if z in vis: return res
        while q:
            nq, res = [], res + 1
            for e in q:
                for i in range(m):
                    for j in range(n):
                        ne=[_[:] for _ in e]
                        for x,y in [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                            if 0<=x<m and 0<=y<n: ne[x][y] ^= 1
                        t = tuple([j for i in ne for j in i])
                        if t == z: return res
                        if t not in vis:
                            vis.add(t)
                            nq.append(ne)
            if not nq: return -1
            q = nq
        return
