# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        global mdep
        mdep = 0
        mdnodes = []
        #print ''

        def lowestCommonAncestor(root, p, q):
            if root in (None, p , q):
                return root

            l = lowestCommonAncestor(root.left, p ,q)
            r = lowestCommonAncestor(root.right, p ,q)

            if l and r:
                return root
            return l or r

        def maxDepth(root):
            def mdepth(root, level):
                global mdep
                if not root:
                    mdep = max(mdep, level)
                    return 0
                return mdepth(root.left, level+1) or mdepth(root.right,level+1)
            mdepth(root, 0)
            return mdep

        def findNodesMaxDepth(root,level):
            if level <= 1 and root:
                mdnodes.append(root)
            if not root: return
            findNodesMaxDepth(root.left, level-1) 
            findNodesMaxDepth(root.right,level-1)
            return

        md =  maxDepth(root)
        #print 'MaxDepth ',md
        findNodesMaxDepth(root, md)
        #print 'Len ',len(mdnodes)
        if len(mdnodes) == 1: 
                return mdnodes[0]
        if len(mdnodes) >= 2: 
                lca = lowestCommonAncestor(root, mdnodes[0], mdnodes[1])
        #print 'Lca1 ', lca.val
        if len(mdnodes) == 2: return lca
        for i in range(2, len(mdnodes)):
            lca = lowestCommonAncestor(root, lca, mdnodes[i])
            #print 'Lca2 ', lca.val

        return lca
        
t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)
t1.left.right = TreeNode(2)
t1.left.left = TreeNode(6)
t1.left.right.left = TreeNode(7)
t1.left.right.right = TreeNode(4)
t1.right.right = TreeNode(8)
t1.right.left = TreeNode(0)
tn = Solution().subtreeWithAllDeepest(t1)
print tn.val

t1 = TreeNode(3)
t1.left = TreeNode(5)
tn = Solution().subtreeWithAllDeepest(t1)
print tn.val

t1 = TreeNode(3)
tn = Solution().subtreeWithAllDeepest(t1)
print tn.val

t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)
t1.left.right = TreeNode(2)
t1.left.left = TreeNode(6)
t1.left.right.left = TreeNode(7)
t1.left.right.right = TreeNode(4)
t1.right.right = TreeNode(8)
t1.right.left = TreeNode(0)
t1.right.left.right = TreeNode(9)
tn = Solution().subtreeWithAllDeepest(t1)
print tn.val

t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)
t1.left.right = TreeNode(2)
t1.left.left = TreeNode(6)
t1.left.right.left = TreeNode(7)
t1.left.right.right = TreeNode(4)
t1.right.right = TreeNode(8)
t1.right.left = TreeNode(0)
t1.left.left.left = TreeNode(9)
tn = Solution().subtreeWithAllDeepest(t1)
print tn.val

t1 = TreeNode(3)
t1.left = TreeNode(5)
t1.right = TreeNode(1)
t1.left.right = TreeNode(2)
t1.left.left = TreeNode(6)
t1.left.right.left = TreeNode(7)
t1.right.right = TreeNode(8)
t1.right.left = TreeNode(0)
tn = Solution().subtreeWithAllDeepest(t1)
print tn.val
