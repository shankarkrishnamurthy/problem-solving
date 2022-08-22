#Fenwick Tree or BIT 
class NumArray:
    def _update(o, i, v):
        diff = v - (o._query(i) - o._query(i-1))
        while i < len(o.bit):
            o.bit[i] += diff
            i += i & -i

    def _query(o, i):
        if i == 0: return 0
        s = 0
        while i:
            s += o.bit[i]
            i -= i & -i
        return s 

    def __init__(o, nums):
        o.bit = [0]*(len(nums)+1)
        for i in range(len(nums)):
            o._update(i+1, nums[i])

    def update(o, index, val):
        o._update(index+1, val)
        print(o.bit)
                
    def sumRange(o, l, r):
        return o._query(r+1) - o._query(l)

obj = NumArray([1,2,3])
print(obj.sumRange(1,2))
obj.update(1,5)
print(obj.sumRange(1,2))

obj = NumArray([1])
print(obj.sumRange(0,0))
obj.update(0,5)
print(obj.sumRange(0,0))
