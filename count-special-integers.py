class Solution:
    def countSpecialNumbers(self, n):
        us, st, nums, res=set(), 1, [int(c) for c in str(n)[::-1]], 0
        for t in range(len(str(n))-1,-1,-1):
            pd = set(range(nums[t]))
            x, st = len(pd - us) - st, 0
            if x != 0:
                res += x*perm(10-len(us)-1, t)
            #print('t', t, 'current # of possibilities', x, 'used set', us, 'total', x*math.perm(10-len(us)-1, t))
            if nums[t] in us: break
            us.add(nums[t])
        rest = sum([9*perm(9, i-1) for i in range(1,len(nums))]) + (len(nums) == len(set(nums)))
        return rest + res
