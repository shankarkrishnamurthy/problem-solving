class Solution:
    def matchPlayersAndTrainers(self, pl, tr):
        pl.sort(), tr.sort()
        res, r = 0, 0
        for i in range(len(pl)):
            while r < len(tr) and tr[r] < pl[i]: r += 1
            if r == len(tr): break
            res, r = res+1, r+1
        return res
            
        
