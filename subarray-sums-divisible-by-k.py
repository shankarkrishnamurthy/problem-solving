class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        cam,s = {},0
        for i in A:
            s += i
            cam[s%K] = cam.setdefault(s%K,0) + 1
        
        #print cam
        s = 0
        for i in range(K):
            if i in cam and cam[i] > 1: 
                s += cam[i] * (cam[i] -1) / 2
        s += cam[0] if 0 in cam else 0
        return s
            


print Solution().subarraysDivByK([4,5,0,-2,-3,1], 5)
