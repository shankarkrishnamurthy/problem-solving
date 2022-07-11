class Solution:
    def idealArrays(self, n, mv):
        def fact(): 
            for i in range(2,mv+1):
                for j in range(1,int(sqrt(i))+1):
                    if i % j != 0: continue
                    for k in set([j, i//j]):
                        if k == i: continue
                        if len(ft[i]) <= len(ft[k]): ft[i] += [0]*(len(ft[k]) - len(ft[i])+1)
                        for ln in range(1, len(ft[k])):
                            if ft[k][ln] == 0: break
                            ft[i][ln+1] += ft[k][ln]
        m, res, ft=10**9+7, 0, [[0,1] for i in range(mv+1)]
        fact() # for e in enumerate(ft): print(e) 
        for i in range(1,mv+1):
            for l in range(1,len(ft[i])): res = (res + ft[i][l]*math.comb(n-1,l-1))%m
            #print("ending with %d array size %d = %d" % (i, n, rc))
        return res

