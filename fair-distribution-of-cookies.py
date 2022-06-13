from itertools import *
class Solution:
    def distributeCookies(self, cokis, k):
        def gsum(l): return sum([cokis[i] for i in l])
        def gmax(l): return max([cokis[i] for i in l])
        def bt(l, msf, k):
            #print('enter', l, k)
            if k == 1: 
                res.append(max(msf, gsum(l)))
                return
            for i in range(len(l)-k+1, len(l)//k-1,-1):
                for cl in combinations(l, i):
                    bt(l-set(cl), max(msf, gsum(cl)), k-1)
            return 
        res = []
        bt(set(range(len(cokis))), 0, k)
        #print('len', len(res), 'val', res)
        return min(res)
    
