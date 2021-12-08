from library_for_lc import *

class Solution:
    def sibconn(self,c):
        p = None
        for i in c:
            if not i: continue
            if not p:
                p = i
                continue
            p.next = i
            p = i
                
    def connect(self, r):
        q= [r]
        while True:
            c = []
            for e in q:
                if e and (e.left or e.right):
                    c += [e.left, e.right]
            if not c: break
            self.sibconn(c)
            q = c
        return r
        
t=deser([1,2,3,4,5,null,7])
o=Solution().connect(t)
print(ser(o))
