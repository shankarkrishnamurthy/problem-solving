from typing import *
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        #top & cw
        d = [1]*8
        sp = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        p,ans= [king[:] for i in range(8)],[]
        qs = set(map(tuple,queens))
        while sum(d):
            for i,v in enumerate(sp):
                if not d[i]: continue
                p[i][0] += v[0]    
                p[i][1] += v[1]    
                if 0<=p[i][0]<8 and 0<=p[i][1]<8:
                    if tuple(p[i]) in qs:
                        d[i]= False
                        ans.append(p[i])
                else: d[i] = False
        return ans
                    
                
print (Solution().queensAttacktheKing(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
print (Solution().queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
print (Solution().queensAttacktheKing(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))
