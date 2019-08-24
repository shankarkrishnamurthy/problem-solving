class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        h,s,c = {v:k for k,v in enumerate(keyboard)},0,0
        for i in word:
            s += abs(c-h[i]) 
            c = h[i]
        return s
        
print Solution().calculateTime(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba")
print Solution().calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode")
