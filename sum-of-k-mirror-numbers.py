from math import *
from collections import deque
from library_for_lc import *
class Solution:
    def palingen(o,k):
        q, od = deque(), []
        for i in range(1,k): 
            q.append(str(i))
            yield str(i)
        while True:
            v = q.popleft()
            yield v+v[::-1]
            for i in range(k):
                od.append(v+str(i)+v[::-1])
            if not q or len(q[-1])*2 > len(od[-1]):
                for i in od: yield i
                od = []
            for i in range(k):
                q.append(v+str(i))

    @timeit
    def kMirror(self, k, n):
        s, i, t = 0, 0, 1
        for t in self.palingen(k):
            nk = int(t, k)
            if str(nk) == str(nk)[::-1]: s, i = s+nk, i+1
            if i >= n: break
        return s
        
for i in range(2,10):
    print("k %d n %d "%( i, 17), end='')
    val = Solution().kMirror(i,17)
    print("res %d\n" % val)

