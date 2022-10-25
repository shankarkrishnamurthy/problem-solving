class Solution:
    def reverseOddLevels(self, root):
        q, odd = [root], True
        while q:
            nq = []
            for i in q:
                if i.left: 
                    nq.append(i.left)
                    nq.append(i.right)
            if not nq: break
            if odd:
                for i in range(len(nq)//2):
                    x, y = nq[i].val, nq[len(nq)-1-i].val
                    nq[i].val, nq[len(nq)-1-i].val = y, x
            q, odd = nq, not odd
        return root
