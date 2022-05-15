class Solution:
    def removeAnagrams(self, words):
        res = [words[0]]
        for i in range(1,len(words)):
            if sorted(res[-1]) == sorted(words[i]): continue
            res.append(words[i])
        return res
        
