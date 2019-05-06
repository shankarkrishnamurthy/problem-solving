# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, r):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.v = 0
        def dfs(r,mi,ma): 
            self.v = max(self.v,abs(ma-mi))
            #print r.val if r else None,mi,ma
            if not r: return
            dfs(r.left, min(mi, r.val), max(r.val,ma))
            dfs(r.right, min(mi, r.val), max(r.val,ma))
            return

        dfs(r,r.val,r.val)
        return self.v
        
from library_for_lc import *
t = deser([8,3,10,1,6,null,14,null,null,4,7,13])
print Solution().maxAncestorDiff(t)
t = deser([8,3,10])
print Solution().maxAncestorDiff(t)
