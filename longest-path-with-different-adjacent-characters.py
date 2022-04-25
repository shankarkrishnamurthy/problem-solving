class Solution:
    def longestPath(self, pa, s):
        class TN():
            def __init__(o, c):  o.cl, o.c = [], c
            def addchild(o, ch): o.cl.append(ch)
        nh, msf = {0: TN(s[0])}, 1
        for i in range(1, len(s)):
            cn = TN(s[i]); nh[i] = cn
        for i in range(1, len(pa)): 
            pn = nh[pa[i]];
            pn.addchild(nh[i])
        def dfs(n):
            nonlocal msf
            ma1, ma2 = 0, 0
            for ch in n.cl:
                l = dfs(ch)
                if ch.c == n.c: continue
                if l > ma1: ma2 = ma1; ma1 = l
                elif l > ma2: ma2 = l
                else: pass
            msf = max(msf, ma1 + ma2 + 1)
            #print('cur', n.c, 'ma1', ma1, 'ma2', ma2, 'msf',msf)
            return ma1 + 1
        dfs(nh[0])
        return msf
