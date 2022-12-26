class Solution:
    def takeCharacters(self, s, k):
        a, b, c = [], [], []
        for i,v in enumerate(s):
            if v == 'a': a.append(i)
            elif v == 'b': b.append(i)
            else: c.append(i)
        if k == 0: return 0
        if len(a) <k or len(b) < k or len(c) < k: return -1
        na, nb ,nc, res  = 0, 0, 0, len(s) - min(a[-k], b[-k], c[-k])
        for i,v in enumerate(s):
            na, nb ,nc = na+(v=='a'), nb+(v=='b'), nc+(v=='c')
            fi1 = a[na-k] if k - na > 0 else len(s)
            fi2 = b[nb-k] if k - nb > 0 else len(s)
            fi3 = c[nc-k] if k - nc > 0 else len(s)
            res = min(res, i+1+len(s) - min(fi1, fi2, fi3))
        return res
