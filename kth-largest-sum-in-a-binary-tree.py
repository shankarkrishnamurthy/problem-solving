class Solution:
    def kthLargestLevelSum(self, root, k):
        q, res = [root], []
        while q:
            nq, t = [], 0
            for i in q:
                if i.left: nq.append(i.left)
                if i.right: nq.append(i.right)
                t += i.val
            res.append(t)
            if not nq: break
            q = nq
        if k > len(res): return -1
        res.sort()
        return res[-k]
