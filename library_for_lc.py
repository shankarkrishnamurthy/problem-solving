import sys
from SameTree import *
import time
def timeit(fn):
    def wrapper(*arg):
        st = time.time()       
        ret = fn(*arg)
        print("Time Taken " ,time.time() - st)
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
class SimpleUnionFind():
    def __init__(o, N):
        o.p,o.w = list(range(N)), [1]*N
    def find(o, x):
        while o.p[x] != x: x = o.p[x]
        return x
    def union(o,a,b):
        x,y = o.find(a), o.find(b)
        if x==y: return
        if o.w[x] < o.w[y]: x,y = y, x
        o.p[y], o.w[x] = x, o.w[x]+o.w[y]
trie = lambda: defaultdict(trie)
root = trie()
(or)
root =  (T := lambda: defaultdict(T))() # oneliner
#r['a'][1] = (1,2)
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

defmax,defmin=0,float("inf") 
# for sum query, uncomment line in query
# replace max -> min below this line
# .,$s/max/min/g
class Node():
    def __init__(o,be,en):
        o.l, o.r = be, en
        o.le, o.ri = None, None
        o.su, o.ma = 0, defmax
    def __str__(o):
        return "[%s sum %d max %d]" % ((o.l,o.r), o.su, o.ma)
        
class ArcaneSegmentTree():
    def __init__(o, l, r, val):
        def build(l,r):
            if l == r:
                n = Node(l,r)
                n.su, n.ma = val, val
                return n
            n, m = Node(l,r), (l+r)//2
            n.le, n.ri = build(l,m), build(m+1,r)
            n.su, n.ma = n.le.su + n.ri.su, max(n.le.ma, n.ri.ma)
            return n
        o.r = build(l,r)

    def query(o, l, r):
        def q(n, f, fn):
            if l > n.r or r < n.l: return defmax
            if l <= n.l and r >= n.r:
                return getattr(n, f)
            a, b = q(n.le, f, fn), q(n.ri, f, fn)
            return fn(a,b)
        #return q(o.r, 'su', lambda x,y: x+y)
        return q(o.r, 'ma', lambda x,y: max(x,y))

    def update(o, ind, val):
        def u(n):
            l, r = n.l, n.r
            if l == r == ind:
                n.su, n.ma = val, val
                return
            m = (l+r)//2
            if ind <= m: u(n.le)
            else: u(n.ri)
            n.su, n.ma = n.le.su + n.ri.su, max(n.le.ma,n.ri.ma)
            return
        u(o.r)
        return

OP=lambda a,b: a+b
#OP=lambda a,b: max(a,b)
class SegmentTree(): # Used for point update
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):                  # Queries in range [l,r)
        l, r, ans = l+self.n, r+self.n, 0
        while l < r:
            if l & 1:
                ans = OP(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = OP(ans, self.tree[r])
            l, r = l>>1, r>>1
        return ans
    
    def update(o, i, val):
        i += o.n
        o.tree[i] = val
        while i > 1:
            i >>= 1
            o.tree[i]=OP(o.tree[i*2], o.tree[i*2+1])
""" EXAMPLE
    st = SegmentTree(13)
    v1=st.query(3,7)
    st.update(5,6)
    v2=st.query(3,7)
"""

# Segment Tree with left index anchored at 0
class SegTreeOneLeg:
    def __init__(self, n: int):
        self.n = 1 << n.bit_length()
        self.tree = [0] * (self.n*2)
    def update(self, ind: int, val: int):
        ind += self.n
        self.tree[ind] = val
        while ind > 1:
            ind //= 2
            self.tree[ind] = max(self.tree[ind*2], self.tree[ind*2+1])
    def query(self, ind: int) -> int:
        ind += self.n
        res = self.tree[ind]
        while ind > 1:
            if ind%2 == 1:
                res = max(res, self.tree[ind-1])
            ind //= 2
        return res

#Fenwick Tree or BIT 
#OP=lambda a,b: a+b
OP=lambda a,b: max(a,b)
class FenwickTree:
    def update(o, i, v):
        i+=1
        while i < len(o.bit):
            o.bit[i] = OP(o.bit[i], v)
            i += i & -i
    def query(o, i):
        i, s = i+1, 0
        while i:
            s = OP(s, o.bit[i])
            i -= i & -i
        return s
    def __init__(o, n): o.bit = [0]*(n+1)
obj = FenwickTree([1,2,3])
print(obj.sumRange(1,2))
obj.update(1,5)
print(obj.sumRange(1,2))

class LazySegmentTree: # Used for Range update
    def __init__(o, n): o.n, o.tree, o.lazy = n, [0]*(4*n), [0]*(4*n)
    def _pushdown(o, v, lo, hi):
        if o.lazy[v]:
            o.tree[v] += (hi - lo + 1) * o.lazy[v]
            if lo < hi:
                o.lazy[2*v + 1] += o.lazy[v]
                o.lazy[2*v + 2] += o.lazy[v]
            o.lazy[v] = 0
    def build(o, arr, v, lo, hi):
        if lo == hi:
            o.tree[v] = arr[lo]
            return
        m = (lo + hi)//2
        o.build(arr, 2*v + 1, lo, m)
        o.build(arr, 2*v + 2, m + 1, hi)
        o.tree[v] = o.tree[2*v + 1] + o.tree[2*v + 2]
    def update(o, v, lo, hi, i, j, val):
        o._pushdown(v, lo, hi)
        if lo > j or hi < i: return 
        if i <= lo and hi <= j: 
            o.lazy[v] = val
            return
        m = (lo + hi)//2
        o.update(2*v + 1, lo, m, i, j, val) 
        o.update(2*v + 2, m+1, hi, i, j, val)
        o.tree[v] = o.tree[2*v + 1] + o.tree[2*v + 2]
    def query(o, v, lo, hi, i, j):
        o._pushdown(v, lo, hi)
        if j < lo or hi < i: return 0
        if i <= lo and hi <= j: return o.tree[v]
        m = (lo + hi)//2
        if i > m: return o.query(2*v + 2, m + 1, hi, i, j)
        elif j <= m: return o.query(2*v + 1, lo, m, i, j)
        return o.query(2*v + 1, lo, m, i, m) + o.query(2*v + 2, m+1, hi, m+1, j)
mx, lst = 10,LazySegmentTree(10)
arr = [random.randint(1,100) for i in range(mx)]
lst.build(arr, 0, 0, mx-1)
print('arr', arr)
lst.update(0,0,mx-1,2,8,2)
lst.update(0,0,mx-1,5,7,3)
print('q2', [3, 7], lst.query(0,0,mx-1,3,8))o

class SegmentTree: # Range update + Diff array + overlap counted once + coordinate compression
    def __init__(self, xs: List[int]):
        self.xs = xs # sorted x coordinates
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)
    
    def update(self, qleft, qright, qval, left, right, pos):
        if self.xs[right+1] <= qleft or self.xs[left] >= qright: # no overlap
            return
        if qleft <= self.xs[left] and self.xs[right+1] <= qright: # full overlap
            self.count[pos] += qval
        else:
            mid = (left + right) // 2
            self.update(qleft, qright, qval, left, mid, pos*2 + 1)
            self.update(qleft, qright, qval, mid+1, right, pos*2 + 2)

        if self.count[pos] > 0: self.covered[pos] = self.xs[right+1] - self.xs[left]
        else:
            if left == right: self.covered[pos] = 0
            else: self.covered[pos] = self.covered[pos*2 + 1] + self.covered[pos*2 + 2]
    
    def query(self): return self.covered[0]

def calculate_z_array(self, s: str) -> list[int]: # Z function
    length = len(s)
    z = [0] * length
    left, right = 0, 0
    for i in range(1, length):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < length and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z

def lps(s): # KMP
    n = len(s)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j and s[i] != s[j]:
            j = lps[j-1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j
return lps

def factorial_mod(n, p):
    fact = [1]*(n+1)
    for i in range(2, n+1): fact[i] = (fact[i-1] * i) % p
    return fact

def factinv_mod(n, p):
    factinv, fact = [1]*(n+1), factorial_mod(n, p)
    for i in range(1,n+1): factinv[i] = pow(fact[i], p-2, p)
    return factinv

def nCr(n, r, p):
    fact, factinv = factorial_mod(n, p), factinv_mod(n, p)
    return (fact[n] * factinv[r] * factinv[n-r]) % p

def lucas_theorem(n: int, k: int, p: int): # see https://en.wikipedia.org/wiki/Lucas%27s_theorem
    product = 1
    while n != 0 or k != 0:
        n_dig = n % p
        k_dig = k % p
        if k_dig > n_dig: return 0
        product *= math.comb(n_dig, k_dig) # for small enough numbers
        product %= p
        n //= p
        k //= p
    return product

def Hierholzer(adj): # Function to print Eulerian circuit
    if len(adj) == 0: return []
    circuit, currPath = [], [0]
    while len(currPath) > 0:
        currNode = currPath[-1]
        if len(adj[currNode]) > 0:
            nextNode = adj[currNode].pop()
            currPath.append(nextNode)
        else: circuit.append(currPath.pop())
    return circuit[::-1]
adj = [[2, 3], [0], [1], [4], [0]]
ans = Hierholzer(adj)
for v in ans: print(v, end=" ")

#LOG = (n).bit_length()     # Binary Lifting
#parent  = [[0]*(n+1) for _ in range(LOG)]
#   using DFS/BFS parent[0][child] = parent
#for k in range(1, LOG):
    #for v in range(1, n+1):
        #parent[k][v] = parent[k-1][parent[k-1][v]]
def lca(u, v): # ancestory using binary lifting
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if diff >> k & 1:
            u = parent[k][u]
    if u == v:
        return u
    for k in reversed(range(LOG)):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]
