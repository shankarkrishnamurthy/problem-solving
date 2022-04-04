class Solution:
    def numberOfWays(self, s):
        n,tn0,tn1,n0,n1,res=len(s),0,0,0,0,0
        for c in s:
            if c == '1': tn1 += 1
            else: tn0+=1
        if s[0] == '0': n0=1
        else: n1=1
        for i in range(1,n-1):
            if s[i] == '0':
                n0 += 1
                res += n1*(tn1 - n1)
            else:
                n1 += 1
                res += n0*(tn0 - n0)
        return res
