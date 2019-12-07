from typing import *
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def isthere(c,w):
            if w[0] in c and w[1] in c and w[2] in c: return True
            return False
        win = [[(0,0),(1,1),(2,2)],[(2,0),(1,1),(0,2)],
                [(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)]]
        a,b=[],[]
        for i in range(0,len(moves),2):
            a.append(tuple(moves[i]))
            if i+1 < len(moves): b.append(tuple(moves[i+1]))
        #print (a,b)
        for l in range(3,6):
            for w in win:
                if isthere(a[:l],w): return 'A'
                if isthere(b[:l],w): return 'B'
        if len(moves) > 8: return 'Draw'
        return 'Pending'

print(Solution().tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
print(Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
print(Solution().tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
print(Solution().tictactoe([[0,0],[1,1]]))
