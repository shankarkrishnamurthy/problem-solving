# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def do_flatten(root):
            if not root:
                return None
            ll = do_flatten(root.left)
            lr = do_flatten(root.right)
            last = root
            if ll:
                root.right = ll
                while ll:
                    last = ll
                    ll = ll.right
            if lr:
                last.right = lr
                while lr:
                    last = lr
                    lr = lr.right
            root.left = None
            return root
        do_flatten(root)
        return

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(5)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right.right = TreeNode(6)
res= Solution().flatten(t1)
while t1:
    print t1.val,t1.left
    t1 = t1.right
print "Done"
