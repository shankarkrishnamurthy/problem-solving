class SnapshotArray(object):
    def __init__(self, length):
        """
        :type length: int
        """
        self.n = length
        self.sid = 0
        self.sh = {}
        self.sh[self.sid] = {}

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        csnap = self.sh[self.sid]
        csnap[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.sid += 1
        self.sh[self.sid] = {}
        return self.sid-1
        

    def get(self, index, snid):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while snid >= 0:
            if index in self.sh[snid]:
                return self.sh[snid][index]
            snid -= 1
        return 0
        
obj = SnapshotArray(10)
obj.set(8,100000)
obj.set(3,90000)
obj.snap() # 0 valid
obj.set(2,90000)
obj.set(3,10000)
obj.set(8,20000)
obj.snap() # 1 valid
print obj.get(8,0)
print obj.get(8,1)
print obj.get(3,0)
print obj.get(3,1)
print obj.get(2,0)
print obj.get(2,1)
