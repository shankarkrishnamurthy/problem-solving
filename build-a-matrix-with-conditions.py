class Solution:
    def buildMatrix(self, k, rc, cc):
        def toposort(q, g, pl):
            l = []
            while q:
                l.append(q.popleft())
                for p in pl[l[-1]]:
                    g[p] -= 1
                    if g[p] == 0: q.append(p)
            return l[::-1]
        gr, gc, pr, pc, qc, qr=defaultdict(int), defaultdict(int), defaultdict(list), defaultdict(list), deque(), deque()
        for a,b in rc: 
            gr[a] += 1 
            pr[b].append(a)
        for l,r in cc: 
            gc[l] += 1
            pc[r].append(l)
        for i in range(1,k+1):
            if gr[i] == 0: qr.append(i)
            if gc[i] == 0: qc.append(i)
        rl, cl, ans, res = toposort(qr, gr, pr), toposort(qc, gc, pc), {i:[0,0] for i in range(1,k+1)}, [[0]*k for _ in range(k)]
        if len(rl) != k or len(cl) != k: return []
        for i, (x,y) in enumerate(zip(rl, cl)): ans[x][0], ans[y][1] = i, i
        for key in ans:
            x,y = ans[key]
            res[x][y] = key
        return res
        
