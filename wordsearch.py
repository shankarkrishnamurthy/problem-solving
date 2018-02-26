import numpy as np
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def do_exist(w, b,r ,c):
            if len(w) == 0:
                print np.array(b)
                return True
            l = []
            if r+1 < len(b) and b[r+1][c] == w[0]:
                l += [(r+1,c)]
            if r-1 >= 0 and b[r-1][c] == w[0]:
                l += [(r-1,c)]
            if c+1 < len(b[0]) and b[r][c+1] == w[0]:
                l += [(r,c+1)]
            if c-1 >= 0 and b[r][c-1] == w[0]:
                l += [(r,c-1)]
            for (i,j) in l:
                tmp = b[i][j]
                b[i][j] = '.'
                if True == do_exist(w[1:],b,i,j):
                    return True
                b[i][j] = tmp

            return False

        if not len(word):
            return ex
        l = [(r,c) for r in range(len(board)) for c in range(len(board[r])) if word[0] == board[r][c]]
        print l
        for (i,j) in l:
            tmp = board[i][j]
            board[i][j]='.'
            if True == do_exist(word[1:], board,i,j):
                return True
            board[i][j]=tmp
        return False

print Solution().exist([ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCCED")
print Solution().exist([ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "SEE")
print Solution().exist([ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], "ABCB")
