class Solution:
    def makeIntegerBeautiful(self, n, target):
        def cnt(n):
            s=[]
            while n: _, n = s.append((n % 10)), n // 10
            return s
        d, co = cnt(n) + [0], 0
        #print('dgt', d)
        if sum(d) <= target: return 0
        for i in range(len(d)-1):
            if co==0 and d[i] == 0: continue
            d[i], co = 0, 1
            v = int(''.join(map(str,d[::-1]))) + co*(10**(i+1))
            #print('i', i, 'd', d, 'co',co, 'v',v)
            if sum(cnt(v)) <= target: break
        return v - n
