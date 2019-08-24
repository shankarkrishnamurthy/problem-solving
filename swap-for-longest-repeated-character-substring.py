class Solution(object):
    def maxRepOpt1(self, t):
        """
        :type t: str
        :rtype: int
        """
        cS , cC, ml,ch =0,t[0],1, {}
        for i in xrange(1,len(t)):
            v = t[i]
            if v!=cC:
                ch.setdefault(cC, []).append((cS,i-1))
                cS,cC = i, v
        ch.setdefault(v, []).append((cS,i))
        print ch
        for c,v in ch.items():
            ml = max(ml, v[0][1]-v[0][0]+1)
            if len(v)>1: ml = max(ml, v[0][1]-v[0][0]+2)
            for i in xrange(1,len(v)):
                x,y = v[i-1]
                a,b = v[i]
                ml = max(ml,b-a+1)
                if y+2 == a:
                    ml = max(ml, b-x + 1) if len(v) > 2 else max(ml,b-x)
                elif len(v) > 1:
                    ml = max(ml,b-a+2)
                
        return ml
           
#print Solution().maxRepOpt1("ababa")
#print Solution().maxRepOpt1("aaabaaa")
#print Solution().maxRepOpt1("aaabbaaa")
#print Solution().maxRepOpt1("aaaaa")
#print Solution().maxRepOpt1("abcdef")
#print Solution().maxRepOpt1("aaabaaaca")
print Solution().maxRepOpt1("aaaaabbbbbbaabbaabbaaabbbbab")
