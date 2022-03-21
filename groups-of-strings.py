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
        #print (self.objects_to_num, sets)
        for i in sets.values(): 
            if i: out.append(repr(i))
        return ', '.join(out)
class Solution:
    def groupStrings(self, wl):
        ht, uf, sl, msf = {}, UnionFind(), {}, 0
        for i, w in enumerate(wl):
            wl[i] = ''.join(sorted(w))
            ht[wl[i]] = i
        for i,w in enumerate(wl):
            if len(w) == 1:
                if 0 not in sl: sl[0] = i
                else: uf.union(sl[0], i)
            else:
                for j in range(len(w)):
                    nw = w[:j] + w[j+1:]
                    nn = len(nw)
                    if nw in ht: uf.union(ht[nw], i)
                    if nn not in sl: sl[nn]={}
                    if nw in sl[nn]: uf.union(sl[nn][nw], i)
                    else: sl[nn][nw] = i 
            msf = max(msf, uf.group_size(i))
        return [len(uf.num_weights), msf]
