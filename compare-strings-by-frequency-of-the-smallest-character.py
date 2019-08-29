from bisect import *
class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def f(w):
            for i in range(ord('a'),ord('z')+1):
                if chr(i) in w: return w.count(chr(i))

        wl = []
        for i in words: wl.append(f(i))
        wl.sort()
        #print 'wl ', wl
        ans = []
        for i in queries:
            c = f(i)
            idx = bisect_right(wl, c)
            #print ' q ',i,' c ', c, 'idx ',idx
            ans.append(len(wl)-idx)
        return ans

print Solution().numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"])
print Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])
