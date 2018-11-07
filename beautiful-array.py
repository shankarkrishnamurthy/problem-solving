class Solution(object):
    def beautifulArray1(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        pend = set(range(1,N-1))
        order = list([N-1,N])
        done = set(order)
        for i in xrange(N-2, 1,-1):
            for j in sorted(pend, reverse=True):
                f = True
                for k in done:
                    e = 2*j - k
                    if e != j and e in pend: f=False
                if f == True: break
            order.append(j)
            done.add(j)
            pend.remove(j)
        order += list(pend)
        return order[::-1]
    def beautifulArray(self, N):
        res = [1]
        while len(res) < N:
            print len(res), res
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        print len(res), res
        return [i for i in res if i <= N]

print Solution().beautifulArray(4)
print Solution().beautifulArray(5)
print Solution().beautifulArray(6)
#print Solution().beautifulArray(7)
