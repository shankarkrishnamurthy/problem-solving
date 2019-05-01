# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, r, v):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        p = h = r
        while r and v < r.val:
            p = r
            r = r.right
        n = TreeNode(v)
        if not r:
            p.right = n
            return h
        if h == r:
            n.left = h
            return n
        p.right = n
        n.left = r
        return h
        
            
      

from library_for_lc import *
t=deser([4,1,3,null,null,2])
o=Solution().insertIntoMaxTree(t, 5)
print ser(o)
t=deser([5,2,4,null,1])
o=Solution().insertIntoMaxTree(t, 3)
print ser(o)
t=deser([5,2,3,null,1])
o=Solution().insertIntoMaxTree(t, 4)
print ser(o)
