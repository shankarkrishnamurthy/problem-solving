import time
import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]] <--- nCk
        """
        def do_combo(m,anc):
            if len(anc) >= k:
                res.append(anc)
                return

            for i in range(m,n+1):
                do_combo(i+1, anc + [i])
            
        res = []
        st = time.clock()
        do_combo(1, []) 
        print time.clock() - st
        return res

    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        st = time.clock()
        l = list(xrange(1, n + 1))
        ll = list(itertools.combinations(l, k))
        print time.clock() - st
        return

print Solution().combine(3,1)
print Solution().combine(5,3)
print Solution().combine(4,2)
#Solution().combine(20,10)
