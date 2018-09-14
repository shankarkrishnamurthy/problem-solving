class ListNode():
    def __init__(self, v):
        self.val = v
        self.next = None

def count(r):
    cnt = 0
    while r:
        cnt += 1 
        r = r.next 
    return cnt

def removeloop(head):
    p, t = head,head
    if not t: return False
    n = head.next
    if not n: return False
    while t and n:
        if t == n:
            print 'converge ', n.val
            newhead = n.next
            n.next = None
            if newhead == n or head == newhead: return True
            n1 = count(head)
            n2 = count(newhead)
            t1,t2 = head, newhead
            while n1 > n2: 
                t1 = t1.next
                n1 -= 1
            while n2 > n1:
                t2 = t2.next
                n2 -= 1
            while t1 != t2:
                p = t2
                t1 = t1.next
                t2 = t2.next
            print ' two list merge point ', t1.val,t2.val
            p.next = None
            while t1 and t1.next: t1 = t1.next
            t1.next = newhead
            
            return True

        t = t.next
        n = n.next
        if not n:
            return False
        else:
            p = n
            n = n.next
    return False

if __name__ == "__main__":
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(6)
    a.next.next.next.next.next.next = ListNode(7)
    a.next.next.next.next.next.next.next = a.next.next.next.next.next.next
    #a.next.next.next.next.next.next.next = a.next.next.next.next.next
    #a.next.next.next.next.next.next.next = a.next.next.next.next
    #a.next.next.next.next.next.next.next = a.next.next.next
    #a.next.next.next.next.next.next.next = a.next.next
    #a.next.next.next.next.next.next.next = a.next
    #a.next.next.next.next.next.next.next = a
    print ' Loop Present ', removeloop(a)
    cnt = 0
    while a and cnt < 20: 
        print a.val, ' -> ',
        cnt += 1
        a = a.next
    print
    if cnt == 20: print ' Wrong '
    
    
