class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        print arr,
        mehwd,meh,msf= -10001,-10001,-10001
        for i,v in enumerate(arr):
            tmeh = meh
            meh = max(meh+v,v)
            if v < 0:
                mehwd = max(tmeh, mehwd+v)
            else:
                mehwd +=v
            msf = max(msf,meh,mehwd)
        return msf

print Solution().maximumSum(arr = [11,-10,-11,8,7,-6,9,4,11,6,5,0])
print Solution().maximumSum(arr = [1,-4,-5,-2,5,0,-1,2])
print Solution().maximumSum(arr = [1])
print Solution().maximumSum(arr = [1,-2])
print Solution().maximumSum(arr = [1,2])
print Solution().maximumSum(arr = [1,-2,0,3])
print Solution().maximumSum(arr = [1,-2,-2,3])
print Solution().maximumSum(arr = [-1,-1,-1,-1])
print Solution().maximumSum(arr = [1,1,1,1])
