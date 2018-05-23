# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def printtn(root):
        print "[",
        q = [root]
        while True:
            nq = []
            for n in q:
                if not n:
                    print 'None,',
                    nq.append(None)
                    nq.append(None)
                    continue
                print n.val,",",
                nq.append(n.left)
                nq.append(n.right)
            while not nq[-1]:
                nq.pop()
                if not nq: break
            if not nq: break
            q = nq
        print "]"


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return root
        parent, node = root,root
        while (node):
            if not node: return root
            if node.val == key:
                break
            elif node.val < key:
                parent = node
                node = node.right
            else:
                parent = node
                node = node.left
        if not node: return root
        #print "found ", node.val, parent.val
        #if node is leaf, noop
        if not node.left and not node.right:
            if parent == node: return None
            if parent.left == node: parent.left = None
            else: parent.right = None
            return root
        #Find next element in subtree
        if not node.right:
            if parent == node: return root.left
            if parent.left == node: parent.left = node.left
            else: parent.right = node.left
            return root
        leftparent = node
        leftmost = node.right
        #print "here " ,leftmost.val, leftparent.val
        while leftmost.left:
            leftparent = leftmost
            leftmost = leftmost.left
        node.val = leftmost.val
        #print "leftmost ", leftmost.val
        if node == leftparent: 
            node.right = leftmost.right
            return root
        else:
            leftparent.left = leftmost.right
            return root

t1 = TreeNode(5)
t1.left = TreeNode(3)
t1.right = TreeNode(8)
t1.left.left = TreeNode(1)
t1.left.left.right = TreeNode(2)
t1.left.right = TreeNode(4)
t1.right.right = TreeNode(9)
#Solution().deleteNode(t1,3)
TreeNode.printtn(t1)
Solution().deleteNode(t1,10)
TreeNode.printtn(t1)
