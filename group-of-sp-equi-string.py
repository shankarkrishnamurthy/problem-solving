class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s=set()
        for i in A:
            ec = sorted(i[::2])
            oc = sorted(i[1::2])
            v = ''.join([i+j for i,j in zip(ec,oc)])
            if len(ec) > len(oc):
                v += ec[-1]
            s.add(v)
            #print 'even', ec, 'odd', oc, 'val ',v
        return len(s)

print Solution().numSpecialEquivGroups(["a","b","c","a","c","c"])
print Solution().numSpecialEquivGroups(["aa","bb","ab","ba"])
print Solution().numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"])
print Solution().numSpecialEquivGroups(["abcd","cdab","adcb","cbad"])
