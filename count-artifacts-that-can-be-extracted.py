class Solution:
    def digArtifacts(self, n, art, dig):
        ah, res=set(), 0
        for i,j in dig: 
            ah.add((i,j))
        for i,j,p,q in art:
            f = True
            for m in range(i, p+1):
                for n in range(j, q+1):
                    if (m,n) not in ah: f = False
            if f: res += 1
        return res
