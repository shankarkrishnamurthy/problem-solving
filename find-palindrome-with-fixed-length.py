class Solution:
    def kthPalindrome(self, ql, il):
        res = []
        if il == 1: return [(i if i < 10 else -1) for i in ql]
        s,e = 10**((il+1)//2-1), 10**((il+1)//2)
        #print('cnt ', e-s, (s,e))
        for v in ql:
            if v > e-s: res.append(-1); continue
            if il % 2 == 0:
                b, m  = 10**(il//2-1) + (v-1), ''
            else:
                x, y = divmod(v-1, 10)
                b, m = 10**(il//2-1) + x, str(y)
            #print('base', b, 'mid', m)
            a = str(b) + m + str(b)[::-1]
            res.append(a)
        return res
