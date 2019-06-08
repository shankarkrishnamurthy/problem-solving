class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        n = max(len(arr1),len(arr2))
        res=[0]*(n+2)
        arr1 = arr1[::-1] 
        arr2 = arr2[::-1]
        for i in xrange(n):
            a = arr1[i] if i < len(arr1) else 0
            b = arr2[i] if i < len(arr2) else 0
            t = a + b + res[i]
            #print i, t
            if t == 2:
                res[i] = 0
                res[i+1] += 1
                res[i+2] += 1
            elif t==3: 
                res[i] = 1
                res[i+1] += 1
                res[i+2] += 1
            elif t==4: 
                res[i] = 0
                res[i+1] += 0
                res[i+2] += 1
            else:
                res[i] = t
        #print res,i
        i+=1
        if res[i] == 2: 
            res[i+1] += 1
            res[i] = 0
        #print res,i
        if res[i+1] == 2: res[i+1] = 0
        #print res, n
        
        res = res[::-1]
        while len(res) > 1:
            if not res[0]: res.pop(0)
            else: break
        return res

print Solution().addNegabinary([1,1,1,1,1], [1,0,1])
print Solution().addNegabinary([1], [1])
print Solution().addNegabinary([0], [0])
print Solution().addNegabinary([1,1], [1])
print Solution().addNegabinary([1,1,1,1,0], [1,1,1,0,0])
