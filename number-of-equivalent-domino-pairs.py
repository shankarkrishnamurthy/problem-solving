class Solution(object):
    def numEquivDominoPairs(self, d):
        """
        :type d: List[List[int]]
        :rtype: int
        """
        h = {}
        for i in d:
            a,b = (i[0],i[1]) if i[0] < i[1] else (i[1],i[0])
            h[(a,b)] = h.get((a,b),0) + 1
        res = 0
        for k in h:
            res += h[k]*(h[k]-1)/2
        return res

print Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]])
print Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[4,3],[3,4]])
