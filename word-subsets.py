class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        univ = []
        bh = dict()
        ah = dict()
        for v in B:
            ch = {}
            for i in v: ch[i] = ch.setdefault(i,0) + 1
            for k in ch:
                if k in bh: bh[k] = max(ch[k],bh[k])
                else: bh.setdefault(k,ch[k])
        for v in A:
            bhcopy = dict(bh)
            for i in v:
                if i in bhcopy:
                    bhcopy[i] -= 1
                    if bhcopy[i] == 0: del bhcopy[i]
            if not bhcopy: univ.append(v)
        return univ
        
print Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"])
print Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"])
print Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","oo"])
print Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])
print Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["ec","oc","ceo"])
print Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["p","pp","e"])
