class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def __init__(self):
        self.hs = dict()

    def do_preorder_dfs(self,root,h):
        if not root:
            return None
        
        if h not in self.hs:
            self.hs.setdefault(h, root.val)

        self.do_preorder_dfs(root.left, h-1)
        self.do_preorder_dfs(root.right, h+1)
        
        return None

    def top_view_list(self, root):
        self.do_preorder_dfs(root,0)
        return [v for k,v in sorted(self.hs.items())]

if __name__ == "__main__":
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(4)
    t.left.left = TreeNode(0)
    t.right.right = TreeNode(5)
    t.right.right.right = TreeNode(6)

    print Solution().top_view_list(t)
