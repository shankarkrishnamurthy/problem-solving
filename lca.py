#!/bin/env python
import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# back path
def findPath(root, n):
    if not root:
        return []

    if (root == n):
        return [root]
    
    val = findPath(root.left, n) or findPath(root.right, n)

    return [root] + val if val else []

#front path
def findPathAnc(root, n, anc):

    if not root:
        return None

    anc.append(root)
    if root == n:
        return root
    val = findPathAnc(root.left, n, anc) or findPathAnc(root.right, n, anc)
    val or anc.pop(-1)
    return anc

def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root or not p or not q:
        None

    #s = findPath(root, p)
    s = findPathAnc(root, p, [])
    #t = findPath(root, q)
    t = findPathAnc(root, q, [])
    for e in s:
        print("%s->" % e.val),
    print ""
    for e in t:
        print("%s->" % e.val),
    print ""
    
    anc = None
    for i,j in zip(s,t):
        if i == j:
            anc = i
        else:
            break;

    return anc
    
if __name__ == "__main__":
    t1 = TreeNode(5)
    t1.left = TreeNode(2)
    t1.right = TreeNode(7)
    t1.left.left = TreeNode(9)
    t1.left.right = TreeNode(1)
    t1.right.right = TreeNode(4)
    t1.left.left.left = TreeNode(3)
    t1.left.left.right = TreeNode(6)
    
    anc = lowestCommonAncestor(t1, t1.left.left.left, t1.left.right) 
    if anc:
        print "Common ancestry: ", anc.val

