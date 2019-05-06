class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        s,res = 0,[]
        for i in A:
            s = (s << 1) | int(i)
            res.append(s % 5 == 0)
        return res

print Solution().prefixesDivBy5([0,1,1])
print Solution().prefixesDivBy5([1,1,1])
print Solution().prefixesDivBy5([0,1,1,1,1,1])
print Solution().prefixesDivBy5([1,1,1,0,1])
