class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            dw, match, seen = {}, True, {}
            for i,c in enumerate(w):
                if pattern[i] not in dw:
                    dw[pattern[i]] = c
                    if c in seen and seen[c] != pattern[i]:
                        match = False
                        break
                    seen[c] = pattern[i]
                elif pattern[i] in dw and c == dw[pattern[i]]:
                    continue
                else:
                    match = False
                    break

            if match: res.append(w)
        return res
            

print Solution().findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")
