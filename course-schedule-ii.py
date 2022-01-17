class Solution:
    def findOrder(self, n, prereq):
        def dfs(e):
            if visit[e] == 1: return True
            if visit[e] == -1: return False
            visit[e] = -1
            for v in g[e]:
                if not dfs(v): return False
            visit[e] = 1
            l.append(e)
            return True

        visit,l = {i:0 for i in range(n)},[]
        g = {i:[] for i in range(n)}
        for i,d in prereq: g[i].append(d)
        for i in g:
            if not dfs(i): return []
        return l

print(Solution().findOrder(3,[]))
print(Solution().findOrder(2,[[0,1]]))
print(Solution().findOrder(2,[[1,0],[0,1]]))
print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
