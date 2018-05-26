class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res,prev = "",0
        indexes, sources, targets = zip(*sorted(zip(indexes,sources,targets)))
        print S,indexes, sources, targets
        for i,v in enumerate(indexes):
            t = len(sources[i])
            if S[v:v+t] == sources[i]:
                res += S[prev:v]
                res += targets[i]
                prev = v+t
            else:
                res += S[prev:v]
                prev = v
            #print i, v, res, prev
        res += S[prev:]
        return res

print Solution().findReplaceString("a", [0], ["a"], ["eee"])
print Solution().findReplaceString("b", [0], ["a"], ["eee"])
print Solution().findReplaceString("abcd", [0,2], ["a","cd"], ["eee","ffff"])
print Solution().findReplaceString("abcd", [0,2], ["ab","ec"], ["eee","ffff"])
print Solution().findReplaceString("vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"])
