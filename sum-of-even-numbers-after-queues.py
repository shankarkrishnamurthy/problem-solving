class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sev = sum([x for x in A if x%2 == 0])
        res = []
        for q in queries:
            v,i = q
            oA = A[i]
            nA = A[i] + v
            if oA%2 == 0: sev -= oA
            if nA%2 == 0: sev += nA
            A[i] = nA
            res += [sev]
        return res
        
print Solution().sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]])
