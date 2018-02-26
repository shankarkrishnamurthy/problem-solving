class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def do_mp(nl):
            if not nl: return 0
            fullprod = 1
            Fo = Lo = -1
            sfeven = True
            for i,v in enumerate(nl):
                if v == 0:
                    if i ==0: maxprod = nl[0]
                    return max(do_mp(nl[i+1:]), 0, maxprod)
                if v<0:
                    sfeven = not sfeven
                    if Fo == -1:
                        Fo = i
                        bfop = fullprod*nl[i]
                    if sfeven == False:
                        Lo = i
                        blop = fullprod*nl[i]
                fullprod *= v
                if sfeven or i == 0:
                    maxprod = fullprod
                else:
                    maxprod = max(maxprod,max(blop, fullprod/blop), fullprod/bfop)
                #print i, " ", maxprod, fullprod, Fo, Lo
            return maxprod

        print nums, ":  ",
        return do_mp(nums)

print Solution().maxProduct([2,3,-2,4])
print Solution().maxProduct([-2,3,2])
print Solution().maxProduct([-2])
print Solution().maxProduct([2,-3,4,-5,6,-7])
print Solution().maxProduct([-1,0,3])
print Solution().maxProduct([0,2])
print Solution().maxProduct([2])
print Solution().maxProduct([0])
print Solution().maxProduct([])
print Solution().maxProduct([-7,6,-5,4,-3,2])
print Solution().maxProduct([1,-2])
print Solution().maxProduct([-3,0,1,-2])
