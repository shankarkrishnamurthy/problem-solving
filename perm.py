class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nlist = []
        def do_permute(e):
            clist=[]
            for i in list(self.nlist):
                for j in xrange(len(i)+1):
                    tmp = list(i)
                    tmp.insert(j, e)
                    print tmp, " " , e
                    clist += [tmp]
            self.nlist = clist
    
        for e in nums:
            if not self.nlist:
                self.nlist = [[e]]
                continue
            do_permute(e)
        return self.nlist

print Solution().permute([1,2,3])
