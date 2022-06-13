class Solution:
    def matchReplacement(self, s, sub, ml):
        mh, plen = defaultdict(set), len(sub)
        for o,n in ml: mh[o].add(n)
        #print(mh)
        for i in range(plen-1, len(s)):
            found = True
            for j in range(plen):
                a,b = s[i-j], sub[plen-j-1]
                #print(a,'sub', b)
                if a!=b and a not in mh[b]: 
                    found = False
                    break
            if found: return True
        return False
