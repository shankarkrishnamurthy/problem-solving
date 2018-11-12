# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root: return 0

        l = self.rangeSumBST(root.left,L,R)
        r = self.rangeSumBST(root.right,L,R)

        return l + r + (root.val if L<= root.val<=R else 0)

t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(15)
t.left.left = TreeNode(3)
t.left.right = TreeNode(7)
t.right.right = TreeNode(18)
print Solution().rangeSumBST(t,7,15)
#Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
#Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(15)
t.left.left = TreeNode(3)
t.left.right = TreeNode(7)
t.right.left = TreeNode(13)
t.right.right = TreeNode(18)
t.left.left.right = TreeNode(6)
print Solution().rangeSumBST(t,6,10)

