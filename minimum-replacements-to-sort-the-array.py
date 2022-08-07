class Solution:
    def minimumReplacement(self, nums):
        msf, res = nums[-1], 0
        for i in range(len(nums)-2,-1,-1):
            v = nums[i]
            if v <= msf:
                msf = v
                continue # already non-decreasing
            q, r = divmod(v, msf)
            if r == 0: res += q-1
            else: msf, res = v//(q+1), q+res
            #print('i', i, 'new msf', msf, '#splits', spl)
        return res
        
