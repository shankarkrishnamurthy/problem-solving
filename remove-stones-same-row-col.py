class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        def dfs(i,j):
            pset.discard((i,j))
            for c in row[i]:
                if (i,c) in pset: dfs(i,c)
            for r in col[j]:
                if (r,j) in pset: dfs(r,j)

        pset,row,col,island = set(list(map(tuple,stones))),{}, {},0
        for i, j in stones:
            row.setdefault(i,[]).append(j)
            col.setdefault(j,[]).append(i)
        for i,j in stones:
            if (i,j) in pset:
                dfs(i,j)
                island += 1

        return len(stones)-island

print Solution().removeStones( [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
print Solution().removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])
print Solution().removeStones([[0,0]])
