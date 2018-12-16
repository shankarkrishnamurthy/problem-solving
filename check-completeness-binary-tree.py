# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, r):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [r]
        nf = False
        while True:
            tmp, f = [], False
            for n in q:
                if n: 
                    if nf: return False
                    f= True
                    tmp.append(n.left)
                    tmp.append(n.right)
                else:
                    nf = True
            if not f: break
            q = tmp
        
        return True
        
    def isCompleteTree1(self, r):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def ict(r):
            def is_power2(num):
	        return num != 0 and ((num & (num - 1)) == 0)
            
            if not r: return (0,0,True)

            lc,lh,lres = ict(r.left)
            rc,rh,rres = ict(r.right)
            print " val ",r.val, "cnt ", lc, rc, ' hgt ', rh,lh

            if not lres or not rres: return (0,0,False)
            if lc < rc: return (0,0,False)
            if lc == rc and not is_power2(lc+1): return (0,0,False)
            if rc < lc and not is_power2(lc+1) and not is_power2(rc+1): return (0,0,False)
            if abs(lh-rh) > 1: return (0,0,False)

            return (lc+rc+1,min(lh,rh)+1,True)

        c,h,res = ict(r)
        print c,h,res
        
        return res
        

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)
t.left.left.left = TreeNode(11)
t.left.left.right = TreeNode(12)
t.left.right.left = TreeNode(13)
t.left.right.right = TreeNode(14)
t.right.left.left = TreeNode(15)
t.right.left.right = TreeNode(16)
t.right.right.left = TreeNode(17)
t.left.left.left.left = TreeNode(19)
print Solution().isCompleteTree(t)
        
