class Solution:
    def minimizeResult(self, expr: str) -> str:
        a,b = expr.split('+')
        msf, l, r = float("inf"), -1, -1
        for i in range(len(a)):
            lm = int(a[:i]) if i > 0 else 1
            for j in range(1,len(b)+1):
                rm = int(b[j:]) if j < len(b) else 1
                val = int(a[i:]) + int(b[:j])
                if msf > float(lm * rm * val):
                    l,r = i, j
                    msf = lm * rm * val
                #print(a[:i]+'('+a[i:]+'+'+b[:j]+')'+b[j:],'msf',float(lm*rm*val))
        return a[:l] + '(' + a[l:] + '+' + b[:r] + ')' + b[r:]
