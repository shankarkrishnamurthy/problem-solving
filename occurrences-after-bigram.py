class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res, l = [],text.split(' ')
        for i in xrange(1,len(l)):
            if l[i-1] == first and l[i] == second:
                if i < len(l)-1: res.append(l[i+1])
        return res
        
print Solution().findOcurrences("alice is a good girl she is a good student",  "a",  "good")
print Solution().findOcurrences("alice is a good girl a good a good student",  "a",  "good")
print Solution().findOcurrences("we will we will rock you", "we", "will")

