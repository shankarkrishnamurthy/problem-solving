from bisect import *
class Solution:
    def maximumSubsequenceCount(self, t, p):
        a,b, res,ch = p[0],p[1], 0,{p[0]:[], p[1]:[]}
        for i in range(len(t)):
            if t[i] == a: ch[a].append(i)
            elif t[i] == b: ch[b].append(i)
            else: pass
        if a == b:
            if len(ch[a]) == 0: return 0
            res = len(ch[a]) * (len(ch[a]) - 1)//2
            return res + len(ch[a])
        for i in ch[a]:
            j = bisect(ch[b], i)
            res += len(ch[b]) - j
        return res + max(len(ch[a]), len(ch[b]))
