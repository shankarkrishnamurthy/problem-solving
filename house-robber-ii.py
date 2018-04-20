# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def do_rob(r):
            if not r: return (0,0)
            lr = do_rob(r.left)
            rr = do_rob(r.right)
            leftggchild = lr[1] - r.left.val if r.left else 0
            rightggchild = rr[1] - r.right.val if r.right else 0
            sumofgrandchilds = max(lr[0] + rr[0], leftggchild + rightggchild, leftggchild+ rr[0],lr[0]+ rightggchild)
            sumofchilds = max(lr[1] + rr[1], lr[1] + rr[0], rr[1] + lr[0])
            return (sumofchilds, sumofgrandchilds + r.val)
        (c,s) = do_rob(root)
        return c if c > s else s
        
"""
t1 = TreeNode(3)
t1.right = TreeNode(5)
t1.left = TreeNode(4)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
t1.right.right = TreeNode(1)
#t1 = TreeNode(3)
#t1.left = TreeNode(2)
#t1.right = TreeNode(3)
#t1.left.right = TreeNode(3)
#t1.right.right = TreeNode(1)
t1 = TreeNode(4)
t1.left = TreeNode(1)
t1.left.left= TreeNode(2)
t1.left.left.left = TreeNode(3)
"""
t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.left.right= TreeNode(4)
t1.right= TreeNode(3)
print Solution().rob(t1)
#[41,37,44,24,39,42,48,1,35,38,40,null,43,46,49,0,2,30,36,null,null,null,null,null,null,45,47,null,null,null,null,null,4,29,32,null,null,null,null,null,null,3,9,26,null,31,34,null,null,7,11,25,27,null,null,33,null,6,8,10,16,null,null,null,28,null,null,5,null,null,null,null,null,15,19,null,null,null,null,12,null,18,20,null,13,17,null,null,22,null,14,null,null,21,23]

