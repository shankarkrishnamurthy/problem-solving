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
        #print self.kv

    def get(self, k, t):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if k not in self.kv: return ""
        i = bisect_left(self.kv[k][0], t)
        #print '\nindx ', i,
        if i >= len(self.kv[k][0]): ts = self.kv[k][0][-1]
        elif t == self.kv[k][0][i]: ts = t
        else:
            if i> 0: ts = self.kv[k][0][i-1]
            else:return ""
            
        return self.kv[k][1][ts]
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
def call(**kwargs):
    print ' Problem '
    for f,v in zip(kwargs["inp"],kwargs["inputs"]):
        if not v: o = eval(f + '()')
        else: 
            print 'Ans ', f, v, getattr(o, f)(*v)

call(inp= ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]])
call(inp= ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]])
