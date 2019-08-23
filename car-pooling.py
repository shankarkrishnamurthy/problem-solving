class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        ev,cur = [],0
        for t in trips:
            c,s,e = t
            ev.append((e,0,c))
            ev.append((s,1,c))
        ev.sort(key = lambda x: (x[0], x[1]))
        print ev
        for i in ev:
            if i[1] == 0:
                cur -= i[2]
            else: cur += i[2]
            print i, cur
            if cur > capacity: return False
        return True
            

print Solution().carPooling([[2,1,5],[3,3,7]], 4)
print Solution().carPooling([[2,1,5],[3,3,7]], 5)
print Solution().carPooling([[2,1,5],[3,5,7]], 3)
print Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11)
