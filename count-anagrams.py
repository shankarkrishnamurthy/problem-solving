class Solution:
    def countAnagrams(self, s):
        @lru_cache(None)
        def fact(n): return math.factorial(n)
        res, m = 1, 1000000007
        for i in s.split():
            cv = 1
            for j,v in Counter(i).items(): cv = cv*fact(v)
            res *= fact(len(i))//cv
            res %= m
        return res
