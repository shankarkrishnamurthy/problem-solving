
class LFUCache(object):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.freq = 1
            self.prev = None
            self.next = None
    def print(o,fn,n):
        while n:
            print(fn,(n.key,n.value,n.freq))
            n = n.next
        
    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node
    
    def insertAt(self, n1, node):
        node.prev = n1.prev
        node.next = n1
        n1.prev.next = node
        n1.prev = node
        return node  

    def __init__(self, capacity):
        self.cnt, self.capacity = 0, capacity
        self.h, self.hf = {}, {}
        self.head, self.tail = self.Node('h', 'h'), self.Node('t', 't')
        self.head.freq, self.tail.freq = -1, -1
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def update(o, key):
        n = o.h[key]
        f = n.freq
        if o.hf[f] == n:
            if n.next.freq == f: o.hf[f] = n.next
            else: o.hf.pop(f)
        f += 1
        n.freq = f
        if f in o.hf:
            n1 = o.hf[f]
        elif f-1 in o.hf:
            n1 = o.hf[f-1]
        else:
            o.hf[f] = n
            return n
        
        n = o.unlink(n)
        o.insertAt(n1,n)
        o.hf[f] = n
        return n
    
    def get(o, key):
        if key not in o.h: return -1
        n = o.update(key)
        #o.print('GET', o.head)
        return n.value

    def put(o, key, value):
        #o.print('PUT',o.head)
        #print(key, value, o.hf.keys())
        if o.capacity == 0: return
        if key in o.h:
            n = o.update(key)
            n.value = value
            return
        o.cnt += 1

        if o.cnt < o.capacity+1:
            n = o.Node(key,value)
            o.h[key] = n
            if 1 not in o.hf:
                o.hf[1] = n
                o.insertAt(o.tail, n)
                return
        else:
            n = o.tail.prev # evict LFU/LRU
            o.h.pop(n.key)
            if o.hf[n.freq] == n: o.hf.pop(n.freq) # last guy
                
            n.key, n.value, n.freq = key, value, 1
            o.h[key] = n
            if 1 not in o.hf:
                o.hf[1] = n
                return
            o.unlink(n)
        
        n1 = o.hf[1]
        #print('TEST', (n1.key,n1.value))
        o.insertAt(n1,n)
        o.hf[1] = n
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
