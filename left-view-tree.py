class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def do_preorder_dfs(self,root,h,res,hs):
        if not root:
            return None
        
        if h not in hs:
            hs.add(h)
            res.append(root.val)

        self.do_preorder_dfs(root.left, h+1, res, hs)
        self.do_preorder_dfs(root.right, h+1, res, hs)
        
        return None

    def left_view_list(self, root):
        res, hs = [], set()
        self.do_preorder_dfs(root,0,res,hs)
        return res

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(4)
    t.right.right = TreeNode(5)
    t.right.right.right = TreeNode(6)

    print Solution().left_view_list(t)
