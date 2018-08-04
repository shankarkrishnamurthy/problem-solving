class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if len(B) <= 1: return A
        b = sorted(enumerate(B), key=lambda x: x[1])
        #print b
        ans, misc = [], []
        ai = 0
        A.sort()
        for i,v in b:
            while ai < len(A):
                if A[ai] > v: 
                    ans.append(A[ai])
                    ai+=1
                    break
                else: 
                    misc.append(A[ai])
                    ai+=1
        fa = ans + misc
        x,y = zip(*sorted(zip(b,fa), key=lambda x:x[0][0]))
        #print y
        return list(y)


print Solution().advantageCount([2],[1])
print Solution().advantageCount([1,2],[1,2])
print Solution().advantageCount([2,7,11,15],[1,10,4,11])
print Solution().advantageCount([12,24,8,32], [13,25,32,11])
print Solution().advantageCount([15777,7355,6475,15448,18412], [986,13574,14234,18412,19893])
