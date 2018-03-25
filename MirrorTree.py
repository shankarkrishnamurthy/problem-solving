# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(l , r):
            if not l and not r:
                return True

            if not l or not r:
                return False
            
            if l.val != r.val: 
                return False
            
            return isSym(l.left, r.right) and isSym(l.right, r.left)
                
        return isSym(root,root)

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(2)
t1.left.right = TreeNode(4)
t1.left.left = TreeNode(3)
t1.right.right = TreeNode(3)
t1.right.left = TreeNode(4)
print Solution().isSymmetric(t1)
