class Solution:
    def minMovesToMakePalindrome(self, s):
        def modify(c, l, f):
            for i in range(l,f): sl[i] = sl[i+1]
            sl[f] = c
        def find(c,r):
            for i in range(r,-1,-1):
                if sl[i] == c: return i
        res, sl, i = 0, list(s), 0
        while i < len(s)//2:
            #print(i, sl)
            c, r= sl[i],len(sl) - i - 1
            ci = find(c, r)
            if ci == i:
                sl[i], sl[i+1],res  = sl[i+1], sl[i], res +1
                continue
            modify(c, ci, r)
            #print('ch ',c, 'ci ', ci, ',di ', r)
            res, i = res+r-ci, i+1
        return res

print(Solution().minMovesToMakePalindrome("skwhhaaunskegmdtutlgtteunmuuludii"))

