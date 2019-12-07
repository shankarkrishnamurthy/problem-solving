from typing import *
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices == 0: return [0,0]
        l,r,n = 0, cheeseSlices+1,cheeseSlices
        while l < r:
            m =  (l+r)//2
            if m*4 + (n-m)*2 == tomatoSlices: return [m,n-m]
            elif m*4 + (n-m)*2 > tomatoSlices: r = m
            else: l = m + 1
        return []
            
        

print(Solution().numOfBurgers(tomatoSlices = 16, cheeseSlices = 7))
print(Solution().numOfBurgers( tomatoSlices = 17, cheeseSlices = 4))
print(Solution().numOfBurgers( tomatoSlices = 4, cheeseSlices = 17))
print(Solution().numOfBurgers( tomatoSlices = 0, cheeseSlices = 0))
print(Solution().numOfBurgers(tomatoSlices = 2, cheeseSlices = 1))
print(Solution().numOfBurgers(tomatoSlices = 4, cheeseSlices = 1))
