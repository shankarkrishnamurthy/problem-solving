# Meeting end and starting at same time are considered overlapping

class Solution():
    def max_meeting_room(self,mlist):
        linlist = []
        for s,e in mlist:
            linlist.append((s,1))
            linlist.append((e,0))

        linlist.sort()
        
        cref,mref = 0,0
        for i in linlist:
            t,v = i
            if v == 0:
                cref -= 1
            else:
                cref += 1
            mref = max(cref, mref)
        
        return mref
        
if __name__ == "__main__":
    print Solution().max_meeting_room([[5,15],[0,8],[10,17],[16,22],[17,23]])
    print Solution().max_meeting_room([[5,15],[6,8],[7,17],[8,22],[9,23]])
    
