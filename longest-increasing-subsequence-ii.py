# Segment Tree (very efficient)
class NumArray:
    def __init__(o, nums):
        def build(i, l, r):
            if l == r:
                o.nl[i] = nums[l]
                return
            build(i*2+1, l, (l+r)//2)
            build(i*2+2, ((l+r)//2)+1, r)
            o.nl[i] = max(o.nl[i*2+1], o.nl[i*2+2])
        o.n, o.nl = len(nums), [0]*4*len(nums)
        build(0, 0, o.n-1)
        
    def update(o, index, val):
        def update(i, l, r ):
            if l == r:
                o.nl[i] = val
                return
            if index <= (l + r)//2: d = update(2*i + 1, l, (l + r)//2)
            else: d = update(2*i + 2, ((l + r)//2)+1, r)
            o.nl[i] = max(o.nl[2*i+1], o.nl[2*i+2])
            return
        update(0, 0, o.n-1)
        #print('update done', o.nl)
                
    def maxRange(o, l, r):
        def query(i, lo, hi, l, r):
            if l > hi or r < lo: return 0
            if lo >=l and hi <=r: return o.nl[i]
            return max(query(i*2+1, lo, (lo + hi)//2, l, r), query(i*2+2, ((lo + hi)//2)+1, hi, l, r))
        res = query(0, 0, o.n-1, max(0,l), r)
        #print('MaxRange done', o.nl)
        return res

class Solution:
    def lengthOfLIS(self, nums, k):
        dp = NumArray([0]*(max(nums)+1))
        for v in nums:
            mv = dp.maxRange(v-k, v-1)
            dp.update(v, 1 + mv)
            print("Max len ending ", v, "is ", 1+mv)
        return dp.maxRange(0,dp.n)

#print(Solution().lengthOfLIS([4,2,1,4,3,4,5,8,15], 3))
print(Solution().lengthOfLIS([7,4,5,1,8,12,4,7], 5))
print(Solution().lengthOfLIS([1,5], 1))

"""
obj = NumArray([0]*8)
print('Max', obj.maxRange(1,2))
obj.update(1,5)
obj.update(2,3)
print('Max',obj.maxRange(1,2))
obj.update(2,8)
print('Max',obj.maxRange(1,2))
obj.update(1,9)
print('Max',obj.maxRange(1,2))
"""
