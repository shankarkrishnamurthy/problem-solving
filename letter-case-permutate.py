class Solution(object):
    def letterCasePermutation(self, S):
        res = [""]
        for i,c in enumerate(S):
            if c.isdigit():
                for i in range(len(res)): res[i] += c
            else:
                nc = c.upper() if c.islower() else c.lower()
                nl,l = list(res),len(res)
                for i in range(l):
                    res[i] += c
                    nl[i] +=  nc
                res += nl
            
        return res

print Solution().letterCasePermutation("")
print Solution().letterCasePermutation("2c4")
print Solution().letterCasePermutation("a2c463B3")
