class StockSpanner(object):
    def __init__(self):
        self.l = []
        self.s = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.l.append(price)
        #print 'price ', price, self.l,' ', self.s, ' val '
        s = 1
        i = len(self.l)-1
        while (i > 0):
            if self.l[i-1] > self.l[len(self.l)-1]:
                break
            c = self.s[i-1]
            #print 'i ', i, ' s', s, ' c ', c
            i -= c
            s += c
        
        self.s.append(s)
        return s


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print obj.next(100)
print obj.next(80)
print obj.next(60)
print obj.next(70)
print obj.next(60)
print obj.next(75)
print obj.next(85)
print obj.next(101)
print obj.next(10)
