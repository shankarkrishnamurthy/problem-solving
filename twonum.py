import sys, os, time
class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {k: v for v, k in enumerate(nums)}
        i = 0
        l = len(nums)
        ans = []
        while i < l:
            j = target - nums[i]
            if d.has_key(j) and i != d[j] and [d[j], i] not in ans:
                ans.append([i, d[j]])
            i+=1
        return ans

    def __init__(self):
        self.list = [i*i for i in range(1, 100)]

    def findAll(self):
        ppt = []
        for t in self.list:
            res = self.twoSum(self.list, t)
            i = 0
            while i < len(res):
                a = res[i][0]+1
                b = res[i][1]+1
                c = self.list.index(t)+1
                i+=1
                if [z for [x,y,z] in ppt if (c%z)==0 and (b%y)==0 and (a%x)==0 and a/x== b/y ]: continue
                ppt.append([a,b,c])
                print "%d,%d,%d" % (a, b, c)

s = Solution()
s.findAll()


