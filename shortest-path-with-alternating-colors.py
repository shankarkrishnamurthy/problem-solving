from typing import *
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        am = {}
        for i in red_edges: am.setdefault((i[0],'b'), []).append((i[1],'r'))
        for i in blue_edges: am.setdefault((i[0],'r'), []).append((i[1],'b'))
        res,cnt = [-1]*n,0
        q,v,res[0] = [(0,'r'),(0,'b')],set(),0
        while q:
            cq,cnt = [],cnt+1
            for i in q:
                v.add(i)
                if i not in am: continue
                for (j,nc) in am[i]:
                    if (j,nc) not in v and nc != i[1]:
                        cq.append((j,nc))
                        if res[j]==-1: res[j] = cnt
            if not cq: break
            q = cq

        return res
        
print(Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[1,2]], blue_edges = []))
print(Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]))
print(Solution().shortestAlternatingPaths(n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]))
print(Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]))
print(Solution().shortestAlternatingPaths(n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]))
