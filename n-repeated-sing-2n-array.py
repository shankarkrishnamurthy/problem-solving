class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        hr = set()
        for i in A:
            if i in hr: return i
            hr.add(i)

print Solution().repeatedNTimes([5,1,5,2,5,3,5,4])
print Solution().repeatedNTimes( [2,1,2,5,3,2])
print Solution().repeatedNTimes([1,2,3,3])
