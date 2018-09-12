class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        d, dh,dv = {int(i):1 for i in D}, {0: 0},{0:0}
        for j in range(1,10): dh[j] = dh[j-1] + (d[j] if j in d else 0)
        for j in range(1,10):
            dv[j] = dv[j-1]
            if j in d: dv[j] = j

        sn = [int(i) for i in str(N)]
        res,ds = 0,set(d)
        mp, mv = dh[9], dv[9]

        #print 'dh ', dh
        #print 'ds ', ds
        #print 'dv ', dv
        #print '--------'

        l,i,went_back,is_all_digit_done = len(sn),0, False,False
        while i < l:
            if i == 0 and dh[sn[i]] == 0:
                del sn[0]
                sn = [mv]*(len(sn))
                is_all_digit_done = True
                break
            while i > 0 and dh[sn[i]] == 0:
                i -= 1
                sn[i] = dv[sn[i]-1] 
                sn = sn[:i+1] + [mv]*(l-i-1)
            if sn[i] not in ds: 
                sn[i] = dv[sn[i]]
                sn = sn[:i+1] + [mv]*(l-i-1)
                continue
            i += 1

        if not is_all_digit_done:
            i = l-1
            while i > -1:
                res += dh[sn[i]]*mp**(l-1-i)
                while i  > 0 and dh[sn[i-1]-1] <=0:
                    i -= 1
                    continue
                if i > 0: sn[i-1] = dv[sn[i-1]-1]
                i -= 1
            if l > 0: del sn[0]

        for i in range(1,len(sn)+1): res += mp**i

        return res

print Solution().atMostNGivenDigitSet(["1","7"], 231)
print Solution().atMostNGivenDigitSet(['1','4','9'],10**9)
print Solution().atMostNGivenDigitSet(["1","3","5","7"], 100)
print Solution().atMostNGivenDigitSet(["3","4","6"], 634)
print Solution().atMostNGivenDigitSet(["3","4","6"], 624)
print Solution().atMostNGivenDigitSet(["1"], 834)
print Solution().atMostNGivenDigitSet(["1"], 1111)
print Solution().atMostNGivenDigitSet(["3","4","5","6"], 624)
print Solution().atMostNGivenDigitSet(["3","4","5","6"], 644)
print Solution().atMostNGivenDigitSet(["3","4","5","6"], 64)
