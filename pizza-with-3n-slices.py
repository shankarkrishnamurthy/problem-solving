class Solution:
    def maxSizeSlices(self, slices):
        @lru_cache(None)
        def walk(i, n):
            if n == 0 or i > len(slices)-1: return 0
            return max(walk(i+1, n), slices[i] + walk(i+2, n-1))
        k= len(slices)//3
        c1 = walk(1, k)
        walk.cache_clear()
        slices[-1] = 0 # slices.pop()
        c2 = walk(0, k)
        return max(c1, c2)
