from bisect import *
class Solution:
    def nextGreatestLetter(self, l, t):
        i = bisect(l, t)
        if i == len(l): i=0
        return l[i]
        
print(Solution().nextGreatestLetter(["c","f","j"], "a"))
print(Solution().nextGreatestLetter(["c","f","j"], "c"))
print(Solution().nextGreatestLetter(["c","f","j"], "d"))
print(Solution().nextGreatestLetter(["c","f","j"], "g"))
print(Solution().nextGreatestLetter(["c","f","j"], "j"))
