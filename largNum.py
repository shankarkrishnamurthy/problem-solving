import functools

def mycmpfn(a,b):
    x = a+b
    y = b+a
    print x," ",y," ",x > y
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0

a=["3"]
a=[]
a=["0", "0"]
a=["343","33","34","32","9", "3"]
print "before ",a
a.sort(cmp=lambda x,y:cmp(y+x, x+y))
print "after ",a
print "Big ", str(int(''.join(a)))
