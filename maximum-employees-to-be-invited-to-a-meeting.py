class Solution:
    def maximumInvitations(self, fav):
        def fillcmf(p , t):
            cnt, r = t[0], t[1]
            while p:
                cnt += 1
                cmf[p.pop()] = (cnt,r)
            cmf[r] = (1,r,max(cmf[r][2], cnt))
            
        def cyclen(p, i ,cnt):
            while p:
                j = p.pop()
                cnt += 1
                if i == j: break
            return 0 if i != j else cnt
        
        def dfs(i, p):
            if i in v:
                if i in cmf: fillcmf(p, cmf[i])
                elif fav[fav[i]] == i:
                    p.pop(); p.pop()
                    cmf[fav[i]], cmf[i] = (1,fav[i],1), (1,i,1)
                    fillcmf(p, cmf[i])
                else: cl[0] = max(cl[0], cyclen(p, i, 0))
            else:
                v.add(i)
                p.append(i)
                dfs(fav[i], p)
            
        cmf, v, cl = {}, set(), [0]
        for i in range(len(fav)):
            if i not in v: dfs(i, [])
        res = sum([cmf[i][2] for i in cmf if len(cmf[i]) > 2])
        return max(res, cl[0])
    
