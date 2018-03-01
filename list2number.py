class LN(object):
    def __init__(self, x):
         self.val = x
         self.next = None

    def __iter__(self):
        LN.node = self
        return self

    def __next__(self):
        tmp =  LN.node
        if not LN.node:
            raise StopIteration
        LN.node = LN.node.next
        return tmp

    next = __next__

    def __str__(self):
        return str(self.val)

def list_to_number(l):
    a = []
    while l:
        a.append(str(l.val))
        l = l.next
    return int(''.join(a)[::-1])
        
def number_to_list(n):
    s = list(str(n)[::-1])
    head = curr = LN(int(s[0]))
    i = 1
    while i < len(s):
            tmp = curr
            curr = LN(int(s[i]))
            tmp.next = curr
            i+=1
    return head

def addTwoNumbers(l1, l2):
    n1 = list_to_number(l1)
    n2 = list_to_number(l2)

    return number_to_list(n1 + n2)

a = LN(9)
b = LN(9)
#c = LN(2)
a.next = b
#b.next = c

x = LN(1)
#y = LN(8)
#z = LN(9)
#x.next = y
#y.next = z

print [ e.val for e in a]
print [ e.val for e in x]
print [ e.val for e in addTwoNumbers(a,x)]
