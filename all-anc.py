class Solution:
    def getAncestors(self, n, edges):
        def dfs(i, chi):
            if i in v:
                for a in chi:
                    res[a].add(i)
                    res[a]=res[a].union(res[i])
                return

            for a in chi: res[a].add(i)
            v.add(i)
            if i not in gout: return
            chi.append(i)
            for e in gout[i]: dfs(e, chi)
            chi.pop()

            return
            
        gout,res,v = {}, [set() for i in range(n)], set()
        for e in edges:
            f,t = e[0],e[1]
            gout.setdefault(t, []).append(f)
        for i in range(n):
            if i not in v: dfs(i, [])
        
        return res

print(Solution().getAncestors(6, [[0,3],[5,0],[2,3],[4,3],[5,3],[1,3],[2,5],[0,1],[4,5],[4,2],[4,0],[2,1],[5,1]]))

