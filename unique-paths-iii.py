class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n, obs = len(grid), len(grid[0]), 0
        for i,r in enumerate(grid):
            for j,v in enumerate(r):
                if v == -1: obs += 1
                if v == 1: st = (i,j)
                if v == 2: en = (i,j)
        t, res, v = m*n - obs, 0, set()
        def dfs(ne):
            nonlocal res
            v.add(ne)
            i,j = ne
            if len(v) == t and ne == en: res += 1
            for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=a<m and 0<=b<n and grid[a][b]!=-1 and (a,b) not in v: dfs((a,b))
            v.remove(ne)
        #print('st', st, 'en', en, 'obs', obs, 't', t)
        dfs(st)
        return res
