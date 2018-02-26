from copy import deepcopy as dc
import numpy as np
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        all = set(['1','2','3','4','5','6','7','8','9'])
        n = 9

        def getrow(tp, i):
            return set(tp[i])

        def getcol(tp, i):
            return set([x[i] for x in tp])

        def getcell(tp, x,y):
            cx=x/3*3
            cy=y/3*3
            return set(np.array(tp)[cx:cx+3, cy:cy+3].flatten().tolist())

        def findnextxy(tp,x,y):
            for x in range(x,n):
                y = y % n
                while y < n:
                    if tp[x][y] == '.': return (x,y)
                    y += 1
            return (x,y)

        def do_sudoku(tp, x, y, board):
            (x,y) = findnextxy(tp,x,y)
            if x==n-1 and y>=n-1 and tp[x][y%n] != '.':
                for i in xrange(n):
                    for j in xrange(n): board[i][j] = tp[i][j]
                return 1

            cl = list(all - getrow(tp,x) - getcol(tp,y) - getcell(tp,x,y))
            for e in cl:
                tp[x][y] = e
                ret = do_sudoku(dc(tp), x, y, board)
                if ret: return ret

            return 0

        do_sudoku(dc(board), 0, 0, board)
        print board

Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])
