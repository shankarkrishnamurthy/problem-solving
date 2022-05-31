class Solution:
    def discountPrices(self, s, d):
        sl, mul = s.split(), (1.0 - d/100.0)
        for i,v in enumerate(sl):
            if v[0] != '$': continue
            try: val = float(v[1:])
            except: continue
            nval = val * mul
            sl[i] = "$%.2f" % nval
        return ' '.join(sl)
        
