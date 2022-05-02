class Solution:
    def maximumMinutes(self, gr):
        def fire(i,j,t): fi[i][j] = t; return 3
        def check(t): return bfs(chk, set([(0,0)]), t)
        def chk(i,j,t):
            nonlocal m,n
            if i==m-1 and j==n-1:
                if fi[i][j] != -1 and t > fi[i][j]: return 0 
                else: return 1
            if fi[i][j] != -1 and t >= fi[i][j]: return 2
            return 3
        def bfs(func, vis, t):
            nonlocal m,n
            ti, q= 0, set(vis)
            while q:
                nq = set()
                for i,j in q:
                    rc = func(i,j,t+ti)
                    if rc == 0 or rc == 1: return rc
                    if rc == 2: continue
                    for a,b in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0<=a<m and 0<=b<n and (a,b) not in vis and gr[a][b]!=2: nq.add((a,b)); vis.add((a,b))
                if not nq: break
                q, ti = nq, ti+1
            return 0
        m, n, q, vis= len(gr), len(gr[0]), [], set()
        fi = [[-1]*n for i in range(m)]
        [vis.add((i,j)) for i in range(m) for j in range(n) if gr[i][j] == 1]
        bfs(fire, vis, 0)
        l, r = 0, max([max(i) for i in fi])
        if not check(0): return -1
        if check(r): return 10**9
        while l < r:
            mid = (l+r)//2
            if check(mid): l = mid+1
            else: r = mid
        return l-1
