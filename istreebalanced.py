# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if not root: return 1
            l = depth(root.left)
            if l < 0: return -1
            r = depth(root.right)
            if r < 0: return -1
            #print "root", root.val, l, r
            if abs(l-r) > 1:
                return -1
            else:
                return l+1 if l > r else r+1
        return False if depth(root) < 0 else True
        
t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(3)
#t1.left.left.left = TreeNode(4)
t1.right = TreeNode(2)
t1.right.right = TreeNode(3)
#t1.right.right.right = TreeNode(4)
print Solution().isBalanced(t1)
