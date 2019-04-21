class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        h = {}
        for i in A[0]: h[i] = h.get(i,0) + 1
        for w in A[1:]:
            n = {}
            for i in w:
                if i not in h: continue
                n[i] = n.get(i, 0) + 1
            for i in h.keys():
                if i not in n:
                    del h[i]
                    continue
                h[i] = min(n[i], h[i])
        res = []
        for i in h:
            res += [i]*h[i]
        return res
        

print Solution().commonChars(["bella","label","rolller"])
print Solution().commonChars(["cool","lock","cook"])
print Solution().commonChars(["a","a"])
print Solution().commonChars(["a","b"])
