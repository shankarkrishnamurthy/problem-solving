class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        q,res = set(),dominoes
        for i,v in enumerate(dominoes):
            if v == 'L' or v == 'R': q.add(i)
        #print res,q
        while True:
            nq,side = set(),'.'
            for e in q:
                if res[e] == 'L':
                    n = e-1
                    side='L'
                elif res[e] == 'R':
                    n = e+1
                    side='R'
                else:
                    print "something wrong"
                if n < 0 or n >= len(res): continue
                #print n,side,nq,res[n]
                if res[n] == '.' or n in nq:
                    if n in nq: 
                        nq.remove(n)
                        res = res[:n] + '.' + res[n+1:]
                    else: 
                        nq.add(n)
                        res = res[:n] + side + res[n+1:]
            #print nq,res
            if not nq: break
            q = nq
        return res

print Solution().pushDominoes(".L.R...LR..L..")
print Solution().pushDominoes("RR.L")
