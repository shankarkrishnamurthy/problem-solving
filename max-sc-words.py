from collections import *
class Solution:
    def maxScoreWords(self, wl, l, sc):
        lh, res, wsh, q = {}, 0, {}, [[]]
        for i in l: lh[i] = lh.get(i,0) + 1
        for w in wl:
            wh = Counter(w)
            if all([k in lh and lh[k] >= wh[k] for k in wh]):
                wsh[w] = sum([wh[k]*sc[ord(k)-ord('a')] for k in wh])
        for w in wl: 
            ss = []
            for i in q:
                nvalid,lhc, cs = False, dict(lh), 0
                for j in i+[w]:
                    wh = Counter(j)
                    if all([k in lhc and lhc[k] >= wh[k] for k in wh]):
                        for k in wh: lhc[k] -= wh[k]
                    else: 
                        nvalid = True
                        break
                    cs += wsh[j]
                if nvalid: continue
                ss += [i + [w]]
                res = max(res, cs)
            q += ss
        
        return res

print(Solution().maxScoreWords(["daeagfh","acchggghfg","feggd","fhdch","dbgadcchfg","b","db","fgchfe","baaedddc"], ["a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d","d","d","e","e","e","e","e","e","e","e","e","e","f","f","f","f","f","f","f","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h","h","h","h","h","h","h"], [2,1,9,2,10,5,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
