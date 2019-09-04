# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from library_for_lc import *
class Solution(object):
    def __init__(self):
        self.h = {}
    def maxLevelSum(self, r):
        """
        :type r: TreeNode
        :rtype: int
        """
        def dfs(r,h):
            if not r: return
            self.h[h] = self.h.get(h,0) + r.val
            dfs(r.left,h+1)
            dfs(r.right,h+1)
            return
        
        dfs(r,1)
        v = max(self.h.values())
        for i in sorted(self.h):
            if self.h[i] == v: 
                #print self.h
                return i

print Solution().maxLevelSum(deser([-8,1,null,2]))
print Solution().maxLevelSum(deser([1,7,0,7,-8,null,null]))
