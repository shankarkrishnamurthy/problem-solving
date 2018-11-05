class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def dfs(a,b,visit,isl):
            visit.add((a,b))
            A[a][b] = isl
            for p,q in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                if 0 <= p < len(A) and 0 <= q < len(A[0]) and (p,q) not in visit and A[p][q] == 1:
                    dfs(p,q,visit,isl)
        
        visit, color = set(), 99
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and (i,j) not in visit:
                    dfs(i,j,visit,color)
                    if color == 99: q = list(visit)
                    color = 199

        print (' q ', q, A)
        visit,cnt = set(),0
        while True:
            tmp = set()
            for c in q:
                visit.add(c)
                a,b = c
                for p,q in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                    if 0 <= p < len(A) and 0 <= q < len(A[0]):
                        if (p,q) not in visit and A[p][q] == 0:
                            tmp.add((p,q))
                        elif A[p][q] == 199:
                            return cnt

            q = tmp
            cnt += 1

print(Solution().shortestBridge([[0,1],[1,0]]))
print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
