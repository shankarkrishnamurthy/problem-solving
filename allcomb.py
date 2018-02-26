import itertools
def subsets1(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    l = [[]]
    l += [[x] for x in nums]
    for i in range(2,len(nums)+1):
        l += [list(x) for x in itertools.combinations(nums,i)]
    return l

class Solution(object):
    
    def __init__(self):
        self.l = [[]]
        
    def do_subsets(self, e):
        c = []
        for i in self.l:
            c += [i + [e]]
        self.l += c

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        for e in nums:
            self.do_subsets(e)
        return self.l
        
print Solution().subsets([])
print Solution().subsets([1])
print Solution().subsets([1,2])
print Solution().subsets([1,2,3])
