class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def getcoord():
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R': return (i,j)

        i,j = getcoord()
        res,U,D,L,R = 0,True,True,True,True
        for k in range(1,8):
            if U and i-k >= 0:
                if board[i-k][j] != '.': U = False
                if board[i-k][j] == 'p': res+=1
            if D and i+k < 8:
                if board[i+k][j] != '.': D = False
                if board[i+k][j] == 'p': res+=1
            if L and j-k >= 0:
                if board[i][j-k] != '.': L = False
                if board[i][j-k] == 'p': res+=1
            if R and j+k < 8:
                if board[i][j+k] != '.': R = False
                if board[i][j+k] == 'p': res+=1
        
        return res

print Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])
print Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])
print Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]])

