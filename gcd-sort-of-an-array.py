class UnionFind():
    def __init__(o, N):
        o.p = list(range(N))
        o.w = [1]*N
    def find(o, x):
        while o.p[x] != x: x = o.p[x]
        return x
    def union(o,a,b):
        x,y = o.find(a), o.find(b)
        if o.w[x] < o.w[y]: x,y = y, x
        o.p[y], o.w[x] = x, o.w[x]+o.w[y]

class Solution:
    def gcdSort(self, nums):
        @lru_cache(None)
        def pFactSet(n):
            for i in range(2,int(math.sqrt(n)) + 1):
                if n % i == 0:
                    yield i
                    while n % i == 0: n //= i
                    if n == 1: break
            if n != 1: yield n

        uf = UnionFind(max(nums) + 1)
        for i in range(len(nums)):
            for p in pFactSet(nums[i]):
                uf.union(nums[i], p)
                
        #print('uf', uf.get())
        for v1,v2 in zip(nums, sorted(nums)):
            if uf.find(v1) != uf.find(v2): return False
        return True
