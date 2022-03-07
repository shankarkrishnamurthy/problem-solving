class Solution:
    def countPoints(self, rings):
        h,cnt = {},set()
        for i in range(0,len(rings),2):
            c,r = rings[i],rings[i+1]
            h.setdefault(r, set()).add(c)
            if len(h[r]) == 3: cnt.add(r)
        return len(cnt)
        

print(Solution().countPoints("B0R0G0R9R0B0G0"))
print(Solution().countPoints("G4"))
