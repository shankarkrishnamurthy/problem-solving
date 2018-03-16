# This tree keeps Big-O(2^n) nodes
# Not suitable for sparse trees
#
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

class Codec(object):
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        print "Serialize: ", root
        res=[]
        q = [root]
        while q:
            nonNone, nq = True, []
            for n in q:
                if not n:
                    nq.append(None)
                    nq.append(None)
                    res.append(None)
                    continue
                nonNone=False
                nq.append(n.left)
                nq.append(n.right)
                res.append(n.val)
            if not nq or nonNone: break
            q = nq
       if res:
           while res[-1] == None:
              res.pop()
              if not res: break
        return repr(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print "Deserialize: ", data
        a = eval(data)
        if not len(a): return None
        root = None
        for i,v in enumerate(a):
            if v == None: continue
            if not root:
                root = TreeNode(v)
                a[0] = root
                continue
            parent = (i-1)/2
            n = TreeNode(v)
            if i % 2 == 0:
                a[parent].right = n
            else:
                a[parent].left = n
            a[i] = n
        return root

# Your Codec object will be instantiated and called as such:
codec = Codec()
"""
#TC1
r=codec.deserialize("[5,None,3,None,None,7,11]")
TreeNode.printtn(r)
print "Deserialize Done"
s=codec.serialize(r)
print "String: ",s
print "Serialize Done"
#TC2
r=codec.deserialize("[]")
TreeNode.printtn(r)
print "Deserialize Done"
s=codec.serialize(r)
print "String: ",s
print "Serialize Done"
#TC3
r=codec.deserialize("[5,None,3,None,None,7,11]")
TreeNode.printtn(r)
print "Deserialize Done"
s=codec.serialize(r)
print "String: ",s
print "Serialize Done"
r=codec.deserialize(s)
TreeNode.printtn(r)
print "Again Deserialize Done"
#TC4
r=codec.deserialize("[None]")
TreeNode.printtn(r)
print "Deserialize Done"
s=codec.serialize(r)
print "String: ",s
print "Serialize Done"
#TC5
r=codec.deserialize("[99]")
TreeNode.printtn(r)
print "Deserialize Done"
s=codec.serialize(r)
print "String: ",s
print "Serialize Done"
"""
#TC6
t1=TreeNode(0)
t1.left=TreeNode(0)
t1.right=TreeNode(0)
t1.left.left=TreeNode(0)
t1.right.right=TreeNode(1)
t1.right.right.right=TreeNode(2)
r=codec.deserialize(codec.serialize(t1))
TreeNode.printtn(r)
print "Deserialize Done"

