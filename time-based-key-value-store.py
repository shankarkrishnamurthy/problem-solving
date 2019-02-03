from bisect import * 
class TimeMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.kv = {}

    def set(self, k, v, t):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if k in self.kv:
            insort(self.kv[k][0],t)
            self.kv[k][1].setdefault(t, v)
        else:
            self.kv[k]=([t],{t:v})

    def get(self, k, t):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if k not in self.kv: return ""
        tl,th = self.kv[k]
        i = bisect_left(tl, t)
        if t >= tl[-1]: ts = tl[-1]
        elif t == tl[i]: ts = t
        else:
            if i>0: ts = tl[i-1]
            else: return ""
            
        return th[ts]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
def call(**kwargs):
    print '-------------'
    for f,v in zip(kwargs["inp"],kwargs["arg"]):
        if f == "TimeMap": o = eval(f+'()')
        else: print f, v, 'Ans:', getattr(o, f)(*v)
    print '-------------'

call(inp= ["TimeMap","set","set","get","get","get","get","get"], arg = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]])
call(inp= ["TimeMap","set","get","get","set","get","get"], arg = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]])
