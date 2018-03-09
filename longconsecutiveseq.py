class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0: return 0
        dv = dict()
        for i,v in enumerate(nums):
            if dv.has_key(v): continue
            c, p, n = i, -1, -1
            if dv.has_key(v-1):
                dv[v-1] = (dv[v-1][0], dv[v-1][1], i)
                p = dv[v-1][0]
            if dv.has_key(v+1):
                dv[v+1] = (dv[v+1][0], i, dv[v+1][2])
                n = dv[v+1][0]
            dv[v] = (i, p, n)
        msf = 1
        for v in nums:
            if dv[v][1] == -1:
                cnt = 1
                ni = dv[v][2]
                while ni != -1:
                    nv = nums[ni]
                    ni = dv[nv][2]
                    cnt += 1
                msf = max(msf, cnt)
        return msf

print Solution().longestConsecutive([0])
print Solution().longestConsecutive([4,3])
print Solution().longestConsecutive([6,41,40])
print Solution().longestConsecutive([100,2,20,1,40,4,2,25,3])
