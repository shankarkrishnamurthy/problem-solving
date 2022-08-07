class Solution:
    def maximumGroups(self, g):
        g.sort()
        s, c= 0, 1
        while s < len(g):
            s += c
            if len(g) - s <= c: break
            c += 1
        return c
