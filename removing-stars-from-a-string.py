class Solution:
    def removeStars(self, s):
        l = []
        for i in s:
            if i != '*': l.append(i)
            else: l.pop()
        return ''.join(l)
        
