class Solution:
    def maximalPathQuality(o, vl, el, mt):
        res, g = 0, {}
        for u,v,t in el:
            g.setdefault(u,[]).append((v,t))
            g.setdefault(v,[]).append((u,t))
        def dfs(i, mt, anc):
            nonlocal res
            if mt < 0: return
            if (i==0):
                res = max(res, sum([vl[k] for k in set(anc)]))
            if i not in g: return
            for j,t in g[i]:
                dfs(j, mt-t, anc + [j])
        dfs(0, mt, [0])
        return res
        
        
