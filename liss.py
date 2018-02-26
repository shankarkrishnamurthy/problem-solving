class Solution():
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for num in nums:
            low, high = 0, len(res)
            while low < high:
                mid = (low+high) / 2
                if res[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            if low == len(res):
                res.append(num)
            else:
                res[low] = num
            print res
        return len(res)
    def lengthOfLIS1(self, nums):
        if not nums:
            return 0
        res=[]
        for i in nums:
            if not res:
                res.append(i)
            elif i < res[0]:
                res[0]=i
            elif i>res[-1]:
                res.append(i)
            else:
                l,r,found=0,len(res)-1,False
                while l<=r:
                    mid=(l+r)/2
                    if res[mid]==i:
                        found=True
                        break
                    elif res[mid]>i:
                        r = mid-1
                    else:
                        l = mid+1
                if not found:
                    res[l]=i
        return len(res)

#print Solution().lengthOfLIS([0, 8, 4, 12, 2])
print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 22])
