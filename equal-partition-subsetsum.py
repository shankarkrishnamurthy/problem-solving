class Solution(object):
    def canPartition(self, nums):
        def canReachSum(nums,S):
            sums = set([S])
            for i in range(len(nums)):
                tmp=set()
                #print sums
                for s in sums:
                    nv = s-nums[i]
                    if nv < 0: continue
                    if nv == 0: 
                        #print i, nums[i]
                        return True
                    tmp.add(nv)
                sums  = sums.union(tmp)
            return False
        t = sum(nums)
        #print nums, t, t/2
        if t % 2 == 1: return False
        return canReachSum(nums, t/2)

    def canPartition1(self, nums):
        def canReachSum(nums,S):
            if S == 0: return True
            if S < 0 or not nums: return False
            return canReachSum(nums[1:], S-nums[0]) or canReachSum(nums[1:],S)
        t = sum(nums)
        print nums, t
        if t % 2 == 1: return False
        return canReachSum(nums, t/2)

    def canPartition2(self, nums):
        def canReachSum(nums,S, sl):
            rotseed = -1
            while rotseed < len(nums):
                print sums, rotseed
                rotseed += 1
                for i in range(len(nums)):
                    r = (i + rotseed) % len(nums)
                    sums[i] += nums[r]
                    if sums[i] == S: 
                        print sums, i
                        return True
            return False
        t = sum(nums)
        print nums, t, t/2, len(nums)
        if t % 2 == 1: return False
        sums = [0]*len(nums)
        return canReachSum(nums, t/2, sums)


print Solution().canPartition([3,5,6,8])
"""
print Solution().canPartition([5,1 ,5,11])
print Solution().canPartition([1, 5,11 ,5])
print Solution().canPartition([1 ,2,3,5])
print Solution().canPartition([2,2,4,4,6])
print Solution().canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100])
print Solution().canPartition([66,90,7,6,32,16,2,78,69,88,85,26,3,9,58,65,30,96,11,31,99,49,63,83,79,97,20,64,81,80,25,69,9,75,23,70,26,71,25,54,1,40,41,82,32,10,26,33,50,71,5,91,59,96,9,15,46,70,26,32,49,35,80,21,34,95,51,66,17,71,28,88,46,21,31,71,42,2,98,96,40,65,92,43,68,14,98,38,13,77,14,13,60,79,52,46,9,13,25,8])
"""
