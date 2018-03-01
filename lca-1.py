#!/bin/env python
import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p , q):
        return root

    l = lowestCommonAncestor(root.left, p ,q)
    r = lowestCommonAncestor(root.right, p ,q)

    if l and r:
        return root

    return l or r
    
if __name__ == "__main__":
    t1 = TreeNode(5)
    t1.left = TreeNode(2)
    t1.right = TreeNode(7)
    t1.left.left = TreeNode(9)
    t1.left.right = TreeNode(1)
    t1.right.right = TreeNode(4)
    t1.left.left.left = TreeNode(3)
    t1.left.left.right = TreeNode(6)
    
    anc = lowestCommonAncestor(t1, t1.left.left.left, t1.left.left.left) 
    if anc:
        print "Common ancestry: ", anc.val

