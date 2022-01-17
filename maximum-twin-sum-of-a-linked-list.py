
class Solution:
    def pairSum(self, head):
        s,f=head,head.next
        while f.next != None:
            s,f = s.next,f.next.next
            
        t,r=None,s.next
        while r !=None:
            n = r.next
            r.next = t
            t = r
            r = n
        msf = 0
        while t:
            msf = max(msf,t.val+head.val)
            t,head = t.next,head.next
        return msf
