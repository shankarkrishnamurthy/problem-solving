class Solution:
    def maximumGood(self, st):
        def check(g):
            for i in range(n):
                if g[i] == '0': continue
                for j,k in enumerate(st[i]):
                    if k == 2: continue
                    if (k==0 and g[j]=='1') or (k==1 and g[j]=='0'):
                        return False
            return True
        n,gu = len(st), []
        for i in range(1<<n, 1<<(n+1)):
            gu.append(bin(i)[3:])
        gu.sort(key=lambda x: x.count('1'), reverse=True)
        for v in gu:
            if check(v): return v.count('1')
        return 0
