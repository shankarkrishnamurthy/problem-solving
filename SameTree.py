# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SameTree(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(2)
    t1.left.right = TreeNode(4)
    t1.left.left = TreeNode(3)
    t1.right.right = TreeNode(3)
    t1.right.left = TreeNode(4)
    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    print SameTree().isSameTree(t1,t2)
