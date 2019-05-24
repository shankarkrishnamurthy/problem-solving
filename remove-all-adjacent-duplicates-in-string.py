class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = [0]
        for i in xrange(1,len(S)):
            if res and S[i] == S[res[-1]]:
                res.pop()
            else:
                res.append(i)
        return ''.join([S[i] for i in res])

print Solution().removeDuplicates("abbaca")
print Solution().removeDuplicates("a")
print Solution().removeDuplicates("aa")
print Solution().removeDuplicates("bab")
print Solution().removeDuplicates("bba")
