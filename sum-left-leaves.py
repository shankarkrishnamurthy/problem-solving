# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sll(root,f):
            if not root: return 0
            l = sll(root.left,1)
            r = sll(root.right,0)

            if not root.left and not root.right and f:
                return root.val
            else:
                return l + r

        return sll(root,0)

t = TreeNode(5)
t.left = TreeNode(3)
t.right = TreeNode(5)
print Solution().sumOfLeftLeaves(t)
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)
print Solution().sumOfLeftLeaves(t)
t = TreeNode(0)
t.left = TreeNode(2)
t.left.left = TreeNode(1)
t.left.left.left = TreeNode(5)
t.left.left.right = TreeNode(1)
t.right = TreeNode(4)
t.right.left = TreeNode(3)
t.right.right = TreeNode(-1)
t.right.left.right = TreeNode(6)
t.right.right.right = TreeNode(8)
print Solution().sumOfLeftLeaves(t)
