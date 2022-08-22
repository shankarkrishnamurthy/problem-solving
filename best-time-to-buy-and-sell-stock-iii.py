class Solution:
    def maxProfit(self, pl):
        n, mi, ma = len(pl), 0, 0
        l, r = [0]*n, [0]*n
        for i in range(1, n):
            if pl[i] < pl[mi]: mi = i
            if pl[i] > pl[ma]: ma = i
            if ma < mi: ma = mi
            l[i] =max(l[i-1], pl[ma] - pl[mi])
            #l[i] =  pl[ma] - pl[mi]
        mi, ma = n-1, n-1
        for i in range(n-2, -1, -1):
            if pl[i] > pl[ma]: ma = i
            if pl[i] < pl[mi]: mi = i
            if mi > ma: mi = ma
            r[i] = max(r[i+1], pl[ma] - pl[mi])
            #r[i] =  pl[ma] - pl[mi]
        #print('l', l, 'r', r)
        #print([a+b for a,b in zip(l, r)])
        return max([a+b for a,b in zip(l, r)])
