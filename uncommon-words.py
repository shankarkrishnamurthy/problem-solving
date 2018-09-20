class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ah = dict()
        for i in A.split(" "):
            ah[i] = ah.setdefault(i, 0) + 1 
        for i in B.split(" "):
            ah[i] = ah.setdefault(i, 0) + 1 
        res = []
        for i in ah:
            if ah[i] == 1:
                res.append(i)
        return res

print Solution().uncommonFromSentences("this apple is sour", "this apple is sweet")
print Solution().uncommonFromSentences("apple apple", "banana")
