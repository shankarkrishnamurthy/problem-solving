class Solution:
    def maximumBobPoints(self, nat, aa):
        def dfs(i, na, anc, val):
            nonlocal res, mval
            if i <=0:
                if mval < val: mval, res = val, anc + [na]
                return
            nw = aa[i]+1
            if na >= nw:
                dfs(i-1, na-nw, anc+[nw], val + i) # bobwins
            dfs(i-1, na, anc+[0], val ) # bobloss
        
        res, mval = [], -1
        dfs(11, nat, [], 0)
        return res[::-1]
