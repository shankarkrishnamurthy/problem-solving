import sys
from SameTree import *
null=None
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def deser(tl):
    p,c = 0,1
    if not tl: return None
    tl[p] = TreeNode(tl[p])
    while p < len(tl):
        if tl[p] == None: 
            p+=1
            continue
        if c >= len(tl): 
            p+=1
            continue
        if tl[c] != None: tl[c] = TreeNode(tl[c])
        tl[p].left = tl[c]
        c+=1
        if c >= len(tl): 
            p+=1
            continue
        if tl[c] != None: tl[c] = TreeNode(tl[c])
        tl[p].right = tl[c]
        c+=1
        p+=1
    return tl[0]

def ser(bt):
    q,res = [bt], []
    while bt:
        nq,idx = [],0
        for p in q:
            res.append(p.val if p else None)
            if not p: continue
            nq.append(p.left)
            nq.append(p.right)
            if not idx and (p.left or p.right): idx=1
        if not nq or idx==0: break
        q = nq 
    return res

def call(**kwargs):
    print '-------------'
    i = 1
    for f,v in zip(kwargs["inp"],kwargs["arg"]):
        if i:
            o = getattr(sys.modules['__main__'], f)()
            i = 0
        else: print f, v, 'Ans:', getattr(o, f)(*v)
    print '-------------'

""" EXAMPLE
t = TreeNode(5)
ds =  ser(t)
print "Deser ", ds
t1 = deser(ds)
print "isSame ", SameTree().isSameTree(t,t1)

call(inp= ["TimeMap","set","set","get","get","get","get","get"], arg = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]])

"""

