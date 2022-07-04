class Solution:
    def maxStudents(self, st):
        m, n, sts = len(st), len(st[0]), set()
        for i in range(m):
            for j in range(n):
                if st[i][j] == '.': sts.add((i,j))
        @lru_cache(None)
        def dfs(r, prev, curr):
            #print('row', r, 'prev', prev, 'curr', curr, tot)
            if r == m: return 0
            tot = 0
            for i in range(1,n+1):
                if (r,i-1) in sts and curr&(7<<i-1)==0 and prev&(5<<i-1) == 0:
                    tot = max(tot, 1+dfs(r, prev, curr|1<<i))
            return max(tot, dfs(r+1, curr, 0))
        return dfs(0, 0, 0)
