# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        lt = self.inorderTraversal(root.left)
        rt = self.inorderTraversal(root.right)
        return lt + [root.val] + rt

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)
print Solution().inorderTraversal(t1)
