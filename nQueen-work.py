import numpy as np
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        anc = ['.' * n for j in range(n)]
        self.N = n
        self.results = []
        def nQueenPossible(anc,i, j):
            n = self.N
            for k in range(n):
                if (anc[i][k] == 'Q' or
                   anc[k][j] == 'Q' or
                   (i+k < n and j+k < n and anc[i+k][j+k] == 'Q') or
                   (i+k < n and j-k >=0 and anc[i+k][j-k] == 'Q') or
                   (i-k >=n and j+k < n and anc[i-k][j+k] == 'Q') or
                   (i-k >=n and j-k >=n and anc[i-k][j-k] == 'Q')):
                    return 0
            return 1
        def do_solve(anc, i):
            for k in range(self.N):
                if nQueenPossible(anc,i, k):
                    anc[i] = anc[i][:k] + 'Q' + anc[i][k+1:]
                    if i == 0:
                        self.results.append(list(anc))
                    else:
                        do_solve(list(anc), i-1)
                    anc[i] = anc[i][:k] + '.' + anc[i][k+1:]
            return

        do_solve(list(anc), n-1)
        print "n=%d Total : %d" % (n, len(self.results))
        return self.results

for i in range(10):
    np.array(Solution().solveNQueens(i))

