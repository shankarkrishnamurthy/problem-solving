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
    def get(self):
        sets = {}
        for i in range(len(self.objects_to_num)): sets[i] = []
        for i in self.objects_to_num: sets[self.objects_to_num[self.find(i)]].append(i)
        return [x for x in sets.values() if x]

class Solution:
    def findAllPeople(self, n, meetings, fp):
        meetings.sort(key=lambda x: x[2])
        luf, v, pt, f = UnionFind(),set([0,fp]), 0, None
        for p1,p2,t in meetings:
            if pt != t:
                if f!=None: [v.add(i) for i in pp if luf.find(i) == luf.find(f)]
                pt, pp, luf, f  = t, [], UnionFind(), None
            if p1 in v or p2 in v:
                if f!=None:
                    luf.union(f, p1)
                    luf.union(f, p2)
                else: f=p1
            luf.union(p1,p2)
            pp += [p1,p2]
            #print((p1,p2,t),'pp',pp,'v',v,'f',f,'uf',luf.get())
        if f!=None:  [v.add(i) for i in pp if luf.find(i) == luf.find(f)]
        return list(v)
