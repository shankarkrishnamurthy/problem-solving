class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        w = set(words)
        for e in list(w):
            for i in range(1,len(e)):
                w.discard(e[i:])
        res = 0
        for i in w:
            res += len(i) + 1
        return  res

print Solution().minimumLengthEncoding(["time","me","bell"])
print Solution().minimumLengthEncoding(["hala","ala","a"])
