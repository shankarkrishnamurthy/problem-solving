#!/bin/env python
def medianval(l):
    ll = len(l)
    return l[ll/2] if ll%2==1 else (l[ll/2] + l[ll/2-1])/2.0
def Lval(l,c):
    if not c.is_integer():
        return l[int(c)]
    return l[int(c-1)] if c>0 else l[int(c)]
def medianCut(l,c):
    if not c.is_integer():
        return l[int(c)]
    else:
        return (l[int(c)] + l[int(c-1)])/ 2.0
def Rval(l,c):
    return l[int(c)]
def islast(l,item):
    i = l.index(item)
    return (i >=(len(l)-1))
def isfirst(l,item):
    i = l.index(item)
    return (i < 1)

def constructList(l1,l2,c1,c2):
    t=int(c1)
    if c1.is_integer():
        left_l1 = l1[0:t-1];
        right_l1 = l1[t+1:len(l1)]
        m_l1 = l1[t-1:t] + l1[t:t+1]
    else:
        left_l1 = l1[0:t];
        right_l1 = l1[t+1:len(l1)]
        m_l1 = l1[t:t+1]
    if len(left_l1) > 0 and len(right_l1) > 0:
        m_l1 += [left_l1[-1]] ; del left_l1[-1]
        m_l1 += [right_l1[0]] ; del right_l1[0]

    t=int(c2)
    if c2.is_integer():
        left_l2 = l2[0:t-1];
        right_l2 = l2[t+1:len(l2)]
        m_l2 = l2[t-1:t] + l2[t:t+1]
    else:
        left_l2 = l2[0:t];
        right_l2 = l2[t+1:len(l2)]
        m_l2 = l2[t:t+1]
    if len(left_l2) > 0 and len(right_l2) > 0:
        m_l2 += [left_l2[-1]] ; del left_l2[-1]
        m_l2 += [right_l2[0]] ; del right_l2[0]

    final = left_l1 + left_l2 + sorted(m_l1 + m_l2) + right_l1 + right_l2
    t= sorted(l1+l2)
    print "Final ", final, " Length " , len(final), " Median ", medianval(final), "PASS" if medianval(final)==medianval(t) else "FAIL"
    assert (len(final) == len(l1) + len(l2))
    return medianval(final)
        
def medianCutVal(l1, l2, c1, c2):
    L1 = Lval(l1,c1); L2 = Lval(l2,c2)
    R1 = Rval(l1,c1); R2 = Rval(l2,c2)
    
    # check if we can move one last time
    if L2 > R1 and not islast(l1,R1) and not isfirst(l2,L2) and medianCut(l1,c1+1.0) < L2 and medianCut(l2,c2-1.0) > R1:
        c1 += 1.0; c2 -= 1.0
    if L1 > R2 and not islast(l2,R2) and not isfirst(l1,L1) and medianCut(l2,c2+1.0) < L1 and medianCut(l1,c1-1.0) > R2:
        c1 -= 1.0; c2 += 1.0

    print "MedianCutVal: c1 ",c1, " c2 ", c2
    m = constructList(l1,l2,c1,c2)

    print "Median: ", m
    print "#Verification",
    t= sorted(a+b)
    print t, len(t), "->  ActualMedian: " ,medianval(t), "PASS" if int(m) == int(medianval(t)) else "FAIL"
    return m

def median(n1, n2):
    # cover base cases
    (l1,l2) = (n2,n1) if len(n1) > len(n2) else (n1,n2)
    if not l1 and not l2:
        return "Wrong. Provide atleast 1 list"
    print "\n",l1,"; Len ", len(l1)
    print l2, "; Len ", len(l2)

    if not (l1 and l2):
        return medianval(l1 or l2)
    len1 = len(l1)
    len2 = len(l2)
    if l1[len1-1] <= l2[0]:
        return medianval(l1 + l2)
    if l2[len2-1] <= l1[0]:
        return medianval(l2 + l1)

    # KEY: always keep the cut in such a way that 
    #   of elements in left = # of elements in right = (m+n)/2
    #   Start from c1 = m/2 and c2=n/2
    c1 = len1/2.0
    c2 = len2/2.0
    mov = max(len1, len2)
    while True:
        # Terminating conditions
        # 1. L1 < R2 and L2 < R1
        # 2. End of a List

        L1 = Lval(l1,c1); L2 = Lval(l2,c2)
        R1 = Rval(l1,c1); R2 = Rval(l2,c2)
        if L1 <= R2 and L2 <= R1:
            return (max(L1 , L2) + min(R1 , R2)) / 2.0 # Simplest of cases

        # Calculate mov positions
        if L1 > R2: # have to move left in l1 and right in l2
            mov1 = c1/2
            mov2 = (len2+c2)/2
            cclock = 1
        else: # have to move right in l1 and left in l2
            mov1 = (len1+c1)/2
            mov2 = c2/2
            cclock = 0
        mov = int(min(abs(c1-mov1), abs(c2-mov2), abs(mov-1)))
        print "Mov ", mov
        if cclock:
            c1 = c1 - mov 
            c2 = c2 + mov 
        else:
            c1 = c1 + mov 
            c2 = c2 - mov 

        if mov == 0 or c1 < 0 or c2 < 0 or c1 > len1-1 or c2 > len2-1:
            return medianCutVal(l1, l2, c1, c2)

a = []; b = [5];
#m = median(a,b)
a = []; b = [5,7,8,9];
m = median(a,b)
a = [1, 3]; b = [2,4];
m = median(a,b)
a = [0, 2,4,6,8,10,14,18,22]; b = [0,1,2,3,4,5,7,9,11,13,15,17,19,21,23,25,27,29];
m = median(a,b)
a = [3,4,6,8]; b = [0,1,2,3,4,5,7,9,11,13,15,17,19,21,23,25,27,29];
m = median(a,b)
a = [2]; b = [1,3,4,5];
m = median(a,b)
a = [2]; b = [1,3,5];
m = median(a,b)
a = [3]; b = [1,2,3,5];
m = median(a,b)
a = [3]; b = [1,2,4];
m = median(a,b)
a = [2]; b = [1,3,4,5,6];
m = median(a,b)
a = [1,3]; b = [2,4,5];
m = median(a,b)
a = [3,4]; b = [1,2,5];
m = median(a,b)
a = [1,2,4]; b = [3,5,6];
m = median(a,b)
a = [1,2,5]; b = [3,4,6]
m = median(a,b)
a = [2]; b = [1,3,4,5,6,7];
m = median(a,b)
a = [1,2,4]; b = [3,5,6,7];
m = median(a,b)
a = [1,2,5]; b= [3,4,6,7];
m = median(a,b)
a = [1,4,5]; b= [3,6,8,9];
m = median(a,b)
a = [5,7,9]; b= [3,4,6,8];
m = median(a,b)
a = [1,2,4]; b = [3,5,6,7,8,9,10]
m = median(a,b)
