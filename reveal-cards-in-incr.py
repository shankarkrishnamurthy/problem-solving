class Solution(object):
    def deckRevealedIncreasing(self, d):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(d)
        d.sort()
        il, c, i = range(n),0,0
        ans = [0]*n
        while c < n-1:
            ans[il[i]] = d[c]
            i += 2
            c += 1
            il.append(il[i-1])
        ans[il[-1]] = d[c]
        return ans
print Solution().deckRevealedIncreasing([17])
print Solution().deckRevealedIncreasing([17,12])
print Solution().deckRevealedIncreasing([17,7,12])
print Solution().deckRevealedIncreasing([17,13,11,2,3,5,7])
print Solution().deckRevealedIncreasing([17,13,11,2,5,7])
