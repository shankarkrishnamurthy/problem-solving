class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        q,visit = {0},set([0])
        while q:
            tmp = set()
            for r in q:
                keys = rooms[r]
                #print r,keys
                for room in keys:
                    if room in visit: continue
                    visit.add(room)
                    tmp.add(room)
            if not tmp: break
            q = tmp
        #print visit
        if set(visit) == set(range(n)):
            return True
        else:
            return False
        

print Solution().canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
print Solution().canVisitAllRooms([[1],[2],[3],[]])
print Solution().canVisitAllRooms([[0]])
