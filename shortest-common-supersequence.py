class Solution:
    def shortestCommonSupersequence(self, s1, s2):
        @lru_cache(None)
        def lcs(i,j):
            if i == len(s1) or j == len(s2): return []
            if s1[i] == s2[j]: 
                return [(i,j)]+lcs(i+1,j+1)
            else:
                v1, v2 = lcs(i,j+1), lcs(i+1,j)
                if len(v1) < len(v2): return v2
                else: return v1
        l, res, x, y = lcs(0,0), "", 0, 0
        #print('list', l)
        for a,b in l:
            res += s1[x:a] + s2[y:b] + s1[a]
            x, y = a+1, b+1
        res += s1[x:len(s1)] + s2[y:len(s2)]
        #print('res', res)
        return res
