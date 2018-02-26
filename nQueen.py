import numpy as np
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        anc = []
        self.N = n
        self.results = []
        def nQueenPossible(anc,i, j):
            for x,y in anc:
                if x==i or j == y:
                    return 0
                if abs(x-i) == abs(y-j):
                    return 0
            return 1

        def do_solve(anc, i):
            for k in range(self.N):
                if nQueenPossible(anc,i,k):
                    anc.append((i,k))
                    if i == 0:
                        self.results.append(list(anc))
                    else:
                        do_solve(list(anc), i-1)
                    anc.pop(-1)
            return

        do_solve(list(anc), n-1)
        print "n=%d Total : %d" % (n, len(self.results))
        return [['.'*i + 'Q' + '.'*(n-i-1) for j,i in s] for s in self.results]

for i in range(10):
    print np.array(Solution().solveNQueens(i))

