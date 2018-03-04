class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fo = dict()
        for v in nums:
            if fo.has_key(v):
                fo[v] += 1
            else:
                fo[v] = 1
        maxe, ele = 0, -1
        for k in fo:
            if fo[k] > maxe:
                ele = k
                maxe = fo[k]
        return ele
