class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        #print A,K
        mrange = A[len(A)-1] - A[0]
        
        if mrange <= K or K == 0: return mrange
        #print 'original range ', mrange, ' var ', K
        for i in range(1,len(A)):
            p = A[i-1] + K
            c = A[i] - K
            #print A[i-1], A[i], ' => ', p,c, ' range ', abs(p-c)
            B=[A[0]+K, c, p, A[len(A)-1]-K]
            B.sort()
            mrange = min(mrange, B[3]-B[0])
        
        return mrange


print Solution().smallestRangeII([2,9,8,0],2) #5
print Solution().smallestRangeII([7,1,10],3) #3
print Solution().smallestRangeII([3021,654,5072,9812,4636,3970,2381,1979,9794,4032],4121) # 4418
print Solution().smallestRangeII([1,6,2,4,8,8],2) #3
print Solution().smallestRangeII([3,1,10],4) #2
print Solution().smallestRangeII([2,7,2],1) #3
print Solution().smallestRangeII([0,10],2) #6
print Solution().smallestRangeII([1,3,6],3) #3
print Solution().smallestRangeII([7,8,8],5) # 1
print Solution().smallestRangeII([7,8,8,5,2],4) #5
print Solution().smallestRangeII([8038,9111,5458,8483,5052,9161,8368,2094,8366,9164,53,7222,9284,5059,4375,2667,2243,5329,3111,5678,5958,815,6841,1377,2752,8569,1483,9191,4675,6230,1169,9833,5366,502,1591,5113,2706,8515,3710,7272,1596,5114,3620,2911,8378,8012,4586,9610,8361,1646,2025,1323,5176,1832,7321,1900,1926,5518,8801,679,3368,2086,7486,575,9221,2993,421,1202,1845,9767,4533,1505,820,967,2811,5603,574,6920,5493,9490,9303,4648,281,2947,4117,2848,7395,930,1023,1439,8045,5161,2315,5705,7596,5854,1835,6591,2553,8628],4643) #8870
