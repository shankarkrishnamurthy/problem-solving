class Solution:
    def equalPairs(self, g):
        n, res, rh = len(g), 0, defaultdict(int)
        for i in g: rh[hash(tuple(i))] += 1
        for j in range(n):
            h = hash(tuple([g[i][j] for i in range(n)]))
            res += rh[h]
        return res
