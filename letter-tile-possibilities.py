import itertools
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        q,a = set([""]),set()
        for t in tiles:
            nl = []
            for l in q:
                nl.append(l+t)
            q=q.union(set(nl))
        q.remove("")
        for w in q: a=a.union(set(itertools.permutations(w)))
        return len(a)

print Solution().numTilePossibilities("CDC")
print Solution().numTilePossibilities("DCC")
print Solution().numTilePossibilities("AAABBCD")
print Solution().numTilePossibilities("AAABBC")
print Solution().numTilePossibilities("AAB")
