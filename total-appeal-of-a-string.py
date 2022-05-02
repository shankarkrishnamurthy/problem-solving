from bisect import *
class Solution:
    def appealSum(self, s):
        vc, res = {}, 0
        for i,v  in enumerate(s):
            app, vc[v]= i+1, i
            for c in vc:
                if c == v: continue
                app += vc[c]+1
            res += app
        return res
