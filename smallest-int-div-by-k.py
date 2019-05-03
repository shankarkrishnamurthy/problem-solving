class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        print 'K ', K,' Ans ',
        i,c,cnt = 1,10%K,1
        while i < K:
            i = i*10+1
            cnt +=1
        if i == K: return cnt
        h,m = {},i%K
        while True:
            v = (m % K) * c + 1
            m = v % K
            cnt +=1
            if m == 0: return cnt
            if m in h: return -1
            h[m] = 1

print Solution().smallestRepunitDivByK(1)
print Solution().smallestRepunitDivByK(3)
print Solution().smallestRepunitDivByK(97)
print Solution().smallestRepunitDivByK(1111)
print Solution().smallestRepunitDivByK(7)
print Solution().smallestRepunitDivByK(17)
print Solution().smallestRepunitDivByK(101)
