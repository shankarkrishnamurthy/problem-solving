class Solution:
    def minimizeSet(self, d1,d2,uc1,uc2):
        def getlast(v,d):
            c, r = divmod(v, d-1)
            if r == 0: return c*d-1
            else: return c*d+r
        tot, lcm = uc1+uc2, math.lcm(d1,d2)
        lv = getlast(tot, lcm)
        val1 = getlast(uc2, d2)
        val2 = getlast(uc1, d1)
        return max(val1,val2,lv)
