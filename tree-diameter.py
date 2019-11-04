from bisect import *
class Solution:
    def __init__(self):
        self.msf = 0
    def treepath(self,e):
        h = {}
        for i in e:
            h.setdefault(i[0],[]).append(i[1])
            h.setdefault(i[1],[]).append(i[0])
        #print(h)
        if not h: return 0

        def dfs(r,v):
            v.add(r)
            p = []
            for i in h[r]:
                if i not in v:
                   insort(p,dfs(i,v))
            if len(p) > 1: m1,m2 = p[-1],p[-2]
            elif len(p) > 0: m1,m2 = p[-1],0
            else: m1 = m2 = 0
            self.msf = max(self.msf, m1 + m2)
            return (1+m1)

        dfs(e[0][0],set())
        return self.msf

print(Solution().treepath([]))
print(Solution().treepath([[0,1],[1,2],[1,3]]))
print(Solution().treepath([[0,1],[1,2],[2,3],[1,4],[4,5]]))
print(Solution().treepath([[0,1],[1,2]]))
