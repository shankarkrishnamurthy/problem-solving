class Solution:
    def maximumSubarraySum(self, nums, k):
        res, l, rs, cs, tot = 0, 0, set(), [], 0
        for i in range(len(nums)):
            rs.add(nums[i])
            tot += nums[i]
            while len(rs) < i - l + 1:
                if nums[i] != nums[l]: rs.remove(nums[l])
                tot -= nums[l]
                l += 1
            if len(rs) > k:
                rs.remove(nums[l])
                tot -= nums[l]
                l += 1
            if len(rs) == k: res = max(res, tot)
            #print('i', i, 'l', l, 'rs', rs, 'res', res)
        return res
