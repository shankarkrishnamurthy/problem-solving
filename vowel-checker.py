import itertools
class Solution(object):
    def spellchecker(self, w, q):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        wh = set()
        lh = {}
        for k,v in enumerate(w):
            if v.lower() not in lh: lh[v.lower()] = k
            wh.add(v)
        res = []
        for i in q:
            if i in wh: 
                res.append(i)
                continue
            
            m = i.lower()
            if m in lh:
                res.append(w[lh[m]])
                continue

            cl = []
            for c in i:
                if c.lower() in ('a','e','i','o','u'):
                    cl.append(['a','e','i','o','u'])
                else:
                    cl.append(c)

            mi = 5001
            D=False
            for e in itertools.product(*cl):
                m = "".join(e).lower() 
                if m in lh:
                    D = True
                    if  lh[m] < mi: mi = lh[m]

            if not D: res.append("")
            else: res.append(w[mi])
                    
        return res
            

print Solution().spellchecker(["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])
print Solution().spellchecker(["ae","aa"], ["UU"])

