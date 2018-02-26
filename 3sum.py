import itertools
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n1_index = [x for x in itertools.combinations(range(len(a)),2)]
        n1 = [x for x in itertools.combinations(a,2)]

print Solution().threeSum([-1, 0, 1, 2, -1, -4])
