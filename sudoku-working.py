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
            cx=int(int(x/3)*3)
            cy=int(int(y/3)*3)
            return set(np.array(tp)[cx:cx+3, cy:cy+3].flatten().tolist())

        def do_sudoku(tp):
            while True:
                cl = []
                for x in range(n):
                    for y in range(n):
                        if tp[x][y] != '.':
                            continue
                        tmp = all - getrow(tp,x) - getcol(tp,y) - getcell(tp,x,y)
                        if len(tmp) == 0:
                            print("Not successful. backtrack, x, y tmp", x,y, tmp)
                            return 0
                        cl.append(((x,y),tmp))

                if len(cl) == 0:
                    for i in range(n):
                        for j in range(n): board[i][j] = tp[i][j]
                    return 1
                cl.sort(key=lambda x:len(x[1]))

                for (i,j), val in cl:
                    print(" i ", i, "j ", j , " v ", val)
                    tmp = all - getrow(tp,i) - getcol(tp,j) - getcell(tp,i,j)
                    if len(tmp) == 0:
                        print("Not successful. Backtrack")
                        return 0
                    if len(val) == 1:
                        tp[i][j] = list(val)[0]
                    else:
                        break

                (i,j), val = cl[0]
                if len(val) > 1:
                    print("Ambiguous State. Fork ", i, " ",j," val ", val)
                    for e in val:
                        tp[i][j] = e
                        print(np.array(tp))
                        ret = do_sudoku(dc(tp))
                        if ret == 1:
                            return ret

        #self.board = board
        do_sudoku(dc(board))
        print(np.array(board))

Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])
