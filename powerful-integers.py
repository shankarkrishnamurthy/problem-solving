import itertools
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        v, val = 1,1
        xl,yl = [],[]
        while val < bound:
            xl.append(val)
            val = x**v
            if xl[-1] == val: break
            v+=1
        v, val = 1,1
        while val < bound:
            yl.append(val)
            val = y**v
            if yl[-1] == val: break
            v+=1
        #print xl,yl
        res = set()
        for i,j in itertools.product(xl,yl): 
            if i+j <= bound: res.add(i+j)
        return list(res)

print Solution().powerfulIntegers(2,1,1000000)
print Solution().powerfulIntegers(3,5,0)
print Solution().powerfulIntegers(3,5,15)
print Solution().powerfulIntegers(2,3,10)
