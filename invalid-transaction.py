class Solution(object):
    def invalidTransactions(self, t):
        """
        :type t: List[str]
        :rtype: List[str]
        """
        i,j,k,l,ans = [],[],[],[],set()
        for x in [y.split(',') for y in t]:
            x1,x2,x3,x4 = x
            i += [x1]
            j += [int(x2)]
            k += [int(x3)]
            l += [x4]
        for c in xrange(len(i)):
            if k[c] > 1000: ans.add(c)
            for r in xrange(c+1,len(i)):
                #print c, i[c],j[c],k[c],l[c]
                if i[c] == i[r] and abs(j[c]-j[r]) <= 60 and l[c] != l[r]:
                    ans.add(r)
                    ans.add(c)
                if k[r] > 1000: ans.add(r)
        ret = [','.join([i[x],str(j[x]),str(k[x]),l[x]]) for x in ans]
        return ret

print Solution().invalidTransactions(["lee,886,1785,beijing","alex,763,1157,amsterdam","lee,277,129,amsterdam","bob,770,105,amsterdam","lee,603,926,amsterdam","chalicefy,476,50,budapest","lee,924,859,barcelona","alex,302,590,amsterdam","alex,397,1464,barcelona","bob,412,1404,amsterdam","lee,505,849,budapest"])
print Solution().invalidTransactions(["bob,627,1973,amsterdam","alex,387,885,bangkok","alex,355,1029,barcelona","alex,587,402,bangkok","chalicefy,973,830,barcelona","alex,932,86,bangkok","bob,188,989,amsterdam"])
print Solution().invalidTransactions(t = ["alice,20,800,mtv","alice,50,100,beijing"])
print Solution().invalidTransactions(t = ["alice,20,800,mtv","alice,50,1200,mtv"])
print Solution().invalidTransactions(t = ["alice,20,800,mtv","bob,50,1200,mtv"])
