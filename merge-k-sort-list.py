from library_for_lc import *
class Solution:
    def mergeKLists(self, ll):
        def mergeTwoLists(l1, l2):
            def addafter(c,l):
                cn = c.next
                c.next = l
                l.next = cn
                return l
            def disconnect(l2):
                d,l2 = l2, l2.next
                return d,l2
            if not (l1 and l2): return l2 or l1
            if l2.val < l1.val: l1,l2 = l2,l1
            h, l1 = disconnect(l1)
            i = h
            while l1 and l2:
                if l1.val < l2.val:
                    d, l1 = disconnect(l1)
                else: 
                    d, l2 = disconnect(l2)
                i = addafter(i,d)
            if l1 or l2: i.next = l1 or l2
            return h

        def merge(a,b):
            m = (a+b)//2
            if a == m:
                return mergeTwoLists(ll[a],ll[b]) if a!=b else mergeTwoLists(ll[m],None)
            s,t = merge(a,m), merge(m+1,b)
            return mergeTwoLists(s,t)
    
        if len(ll) < 1: return []
        return merge(0,len(ll)-1)

print(prll(Solution().mergeKLists([arr2ll([1,4,5]),arr2ll([1,3,4]),arr2ll([2,6])])))
print(prll(Solution().mergeKLists([arr2ll([1,4,5]),arr2ll([1,3,4]),arr2ll([2,6])])))
