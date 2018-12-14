class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ri = {v:i for i,v in enumerate(order)}
        for i in range(1,len(words)):
            w1 = words[i-1]
            w2 = words[i]
            #print zip(w1,w2)
            suc = False
            for a,b in zip(w1,w2):
                if ri[a] > ri[b]: return False        
                if ri[a] < ri[b]: 
                    suc = True
                    break
            if not suc and len(w1) > len(w2): return False
        return True
        
print Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
print Solution().isAlienSorted(["word","world","row"],"worldabcefghijkmnpqstuvxyz")
print Solution().isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz")
