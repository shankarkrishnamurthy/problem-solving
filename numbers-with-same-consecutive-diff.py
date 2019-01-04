class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N==1: return range(0,10)
        s = set(range(0,10))
        nos=[]
        for i in range(1,10):
            if (i+K) in s or (i-K) in s:
                nos.append(str(i))
        d = 1
        while d < N:
            tmp = set()
            #print nos
            for i in nos:
                d1,d2 = int(i[-1])-K, int(i[-1])+K
                #print i, d1,d2
                if d1 in s: tmp.add(i + str(d1))
                if d2 in s: tmp.add(i + str(d2))
            nos = list(tmp)
            d+=1
        return map(int,nos)

print Solution().numsSameConsecDiff(1,0)
print Solution().numsSameConsecDiff(9,0)
print Solution().numsSameConsecDiff(9,1)
print Solution().numsSameConsecDiff(9,2)
print Solution().numsSameConsecDiff(9,3)
print Solution().numsSameConsecDiff(9,4)
print Solution().numsSameConsecDiff(9,5)
print Solution().numsSameConsecDiff(3,7)
print Solution().numsSameConsecDiff(2,1)
