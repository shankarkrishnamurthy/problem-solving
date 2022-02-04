import sys
from SameTree import *
import time
def timeit(fn):
    def wrapper(*arg):
        st = time.clock()       
        ret = fn(*arg)
        print("Time Taken " ,time.clock() - st)
        return ret
    return wrapper
null=None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def prll(h):
    a = []
    while h:
        a.append(h.val)
        h = h.next
    return a
def arr2ll(a):
    head = tail = None
    for i in a:
        l = ListNode(i)
        if not head:
            head = tail = l
        else:
            tail.next = l
            tail = tail.next
    return head

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
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
    print('-------------')
    i = 1
    for f,v in zip(kwargs["inp"],kwargs["arg"]):
        if i:
            o = getattr(sys.modules['__main__'], f)(*v)
            i = 0
        else: print (f, v, 'Ans:', getattr(o, f)(*v))
    print ('-------------')

""" EXAMPLE
t = TreeNode(5)
ds =  ser(t)
print "Deser ", ds
t1 = deser(ds)
print "isSame ", SameTree().isSameTree(t,t1)

call(inp= ["TimeMap","set","set","get","get","get","get","get"], arg = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]])

"""
class UnionFind:
    def __init__(self):
        self.num_weights = {}
        self.parent_pointers = {}
        self.num_to_objects = {}
        self.objects_to_num = {}
        self.__repr__ = self.__str__
    def find(self, object):
        if not object in self.objects_to_num:
            obj_num = len(self.objects_to_num)
            self.num_weights[obj_num] = 1
            self.objects_to_num[object] = obj_num
            self.num_to_objects[obj_num] = object
            self.parent_pointers[obj_num] = obj_num
            return object
        stk = [self.objects_to_num[object]]
        par = self.parent_pointers[stk[-1]]
        while par != stk[-1]:
            stk.append(par)
            par = self.parent_pointers[par]
        for i in stk: self.parent_pointers[i] = par
        return self.num_to_objects[par]
    def union(self, object1, object2):
        o1p = self.find(object1)
        o2p = self.find(object2)
        if o1p != o2p:
            on1 = self.objects_to_num[o1p]
            on2 = self.objects_to_num[o2p]
            w1 = self.num_weights[on1]
            w2 = self.num_weights[on2]
            if w1 < w2:
                o1p, o2p, on1, on2, w1, w2 = o2p, o1p, on2, on1, w2, w1
            self.num_weights[on1] = w1+w2
            del self.num_weights[on2]
            self.parent_pointers[on2] = on1
    def group_size(self, object1):
        o1p =  self.find(object1)
        on1 = self.objects_to_num[o1p]
        return self.num_weights[on1]
    def __str__(self):
        sets = {}
        for i in range(len(self.objects_to_num)): sets[i] = []
        for i in self.objects_to_num: sets[self.objects_to_num[self.find(i)]].append(i)
        out = []
        print (self.objects_to_num, sets)
        for i in sets.values(): 
            if i: out.append(repr(i))
        return ', '.join(out)
    def get(self):
        sets = {}
        for i in range(len(self.objects_to_num)): sets[i] = []
        for i in self.objects_to_num: sets[self.objects_to_num[self.find(i)]].append(i)
        return [x for x in sets.values() if x]
    def getlist(self, obj):
        sets, o = [], self.find(obj)
        for i in self.objects_to_num:
            if self.find(i) == o: sets.append(i)
        return sets
class Trie:
    def __init__(o, w=[]):
        o.r = {}
        for i in w: o.create(i)
    def create(o, w):
        #print("create " , w)
        cr = o.r
        for c in w:
            cr[c] = cr.setdefault(c, {})
            cr[c]['P'] = cr
            cr = cr[c]
        cr['#'] = None
    def delete(o, w):
        #print("delete " , w)
        cr,i  = o.r, len(w)-1
        for c in w:
            if c in cr: cr = cr[c]
            else: return 
        if '#' not in cr: return
        del cr['#']
        while 'P' in cr:
            cr = cr['P']
            if len(cr[w[i]]) > 1: break
            del cr[w[i]]
            i -= 1
    def check(o, w):
        #print("check " , w)
        cr = o.r
        for c in w:
            if c in cr: cr = cr[c]
            else: return False
        if '#' not in cr: return False
        return True
