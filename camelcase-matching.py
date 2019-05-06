class Solution(object):
    def camelMatch(self, q, p):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        res = []
        for w in q:
            #print w,p,
            i, j = 0,0
            while i < len(w) and j < len(p):
                #print i,j
                if 'A'<=w[i]<='Z':
                    if p[j] != w[i]: break
                    i += 1
                    j += 1
                else:
                    if w[i] == p[j]:
                        j+=1
                    i += 1
            while i < len(w):
                if 'A' <= w[i] <= 'Z': break
                i += 1
            res.append(j==len(p) and i==len(w))
        return res

print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB")
print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa")
print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT")
print Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack","FBa"], "FoBa")
