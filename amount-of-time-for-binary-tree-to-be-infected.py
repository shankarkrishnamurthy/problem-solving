class Solution:
    def amountOfTime(self, root, st):
        res, sth= None, -1
        def walk(r, h):
            nonlocal res, sth
            if not r: return (0,0,0)
            le, ri = walk(r.left, h+1), walk(r.right, h+1)
            lh = max(le[0], le[1]) + (r.left != None)
            rh = max(ri[0], ri[1]) + (r.right != None)
            if r.val == st: 
                sth, res = h, max(lh, rh)
            if le[2]: res = max(res, abs(h-sth) + rh)
            elif ri[2]: res = max(res, abs(h-sth) + lh)
            fnd = int(r.val == st or le[2] or ri[2])
            return (lh, rh, fnd)
        walk(root, 0)
        return res
