class Solution:
    def minInsertions(self, s):
        @lru_cache(None)
        def walk(i,j):
            if i>=j: return 0
            
            if s[i] == s[j]:
                return walk(i+1, j-1)
            else:
                return 1+ min(walk(i, j-1), walk(i+1, j))
    
        s = list(s)
        rc = walk(0, len(s)-1)
        return rc
