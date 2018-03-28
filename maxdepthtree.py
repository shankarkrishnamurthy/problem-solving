# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.mdep = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def mdepth(root, level):
            if not root:
                self.mdep = max(self.mdep, level)
                return 0
            return mdepth(root.left, level+1) or mdepth(root.right,level+1)
            
        mdepth(root, 0)
        return self.mdep

#t1 = TreeNode(1)
#t1.left = TreeNode(1)
#t1.left.left = TreeNode(1)
print Solution().maxDepth(t1)
