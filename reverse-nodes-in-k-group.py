class Solution:
    def reverseKGroup(self, head, k):
        def reverse(oh, ot):
            t, nt, ot.next = None, oh, None
            while nt:
                t1, nt.next = nt.next, t
                t, nt = nt, t1
            return (ot, oh) # nh, nt
        if k == 1: return head
        t, oh, c, res = head, head, 0, []
        while t:
            c += 1
            if c == k:
                ot, t1 = t, t.next
                nh, nt = reverse(oh,ot)
                res.append((nh,nt))
                oh, t, ot, c = t1, t1, None, 0
            else: t = t.next
        if oh: res.append((oh, None))
        for i in range(1, len(res)):
            pt, ch = res[i-1][1], res[i][0]
            pt.next = ch
        return res[0][0]
