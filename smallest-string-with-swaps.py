from typing import *
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
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind()
        for p in pairs:
            uf.union(p[0],p[1])
        a = uf.get()
        ans = list(s)
        for i in a:
            i.sort(key=lambda x: s[x])
            b = sorted(i)
            for (j,k) in zip(b,i): ans[j] = s[k]
        #print(a)
        return ''.join(ans)
        
        
print(Solution().smallestStringWithSwaps(s = "dcab", pairs = []))
print(Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
print(Solution().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
print(Solution().smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))
