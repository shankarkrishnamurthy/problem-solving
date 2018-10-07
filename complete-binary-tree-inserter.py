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


class CBTInserter(object):
    def __init__(self, root):
        def getanc(root,ln,a):
            if not root: return None
            if root == ln: return a
            a.append(root)
            l = getanc(root.left,ln, a)
            if l: return l
            r = getanc(root.right,ln, a)
            if r: return r
            a.pop()
            return None
        self.root = root
        self.poftwo = set()
        for i in range(1,20): self.poftwo.add(2**i-1)
        q,cnt = [root],0
        while True:
            tmp = list()
            for n in q:
                lastnode = n
                cnt += 1
                if n.left: tmp.append(n.left)
                if n.right: tmp.append(n.right)
            if not tmp: break
            q = tmp
        self.len = cnt
        self.anc = getanc(root,lastnode,[])

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        head = self.root
        if self.len in self.poftwo:
            head,self.anc = self.root,[self.root]
            while head.left != None: 
                head = head.left
                self.anc.append(head)
            head.left = TreeNode(v)
        else:
            head = self.anc[-1]
            if not head.right:
                head.right = TreeNode(v)
            else:
                for i in range(len(self.anc)-2,-1,-1):
                    cn = self.anc[i]
                    if cn.left == self.anc[i+1]: break
                self.anc[i+1] = cn.right
                head = cn.right
                i += 2
                while head.left:
                    self.anc[i] = head.left
                    i += 1
                    head = head.left
                head.left = TreeNode(v)

        self.len += 1
        return head.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
        
#inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
#inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]

# Your CBTInserter object will be instantiated and called as such:
root=TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
obj = CBTInserter(root)
param_1 = obj.insert(100)
param_1 = obj.insert(101)
param_2 = obj.get_root()
TreeNode.printtn(param_2)

