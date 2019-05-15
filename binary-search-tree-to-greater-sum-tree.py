# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from library_for_lc import *

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.tot = 0;
        def totbst(r):
            if not r: return 0
            lv = totbst(r.left)
            rv = totbst(r.right)
            return lv+r.val+rv
        self.tot = totbst(root)
        def dfs(r, cv):
            if not r: return 0
            lv = dfs(r.left, cv)
            nv = cv - lv
            myv = r.val
            rv = dfs(r.right, cv - lv - r.val)
            r.val = nv
            return lv + myv + rv

        dfs(root, self.tot)
        return root
        
t = Solution().bstToGst(deser([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]))
print ser(t)
t = Solution().bstToGst(deser([4]))
print ser(t)
