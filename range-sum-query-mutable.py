# Segment Tree
class NumArray:
    def __init__(o, nums):
        def build(i, l, r):
            if l == r:
                o.nl[i] = nums[l]
                return
            m = (l+r)//2
            build(i*2+1, l, m)
            build(i*2+2, m+1, r)
            o.nl[i] = o.nl[i*2+1] + o.nl[i*2+2]
        
        o.n, o.nl = len(nums), [0]*4*len(nums)
        build(0, 0, o.n-1)
        
    def update(o, index, val):
        def update(i, l, r ):
            if l == r:
                old, o.nl[i] = o.nl[i], val
                return val - old
            m = (l + r)//2
            if index <= m: d = update(2*i + 1, l, m)
            else: d = update(2*i + 2, m+1, r)
            o.nl[i] += d
            return d
        #print('update ', o.nl)
        update(0, 0, o.n-1)
                
    def sumRange(o, l, r):
        def query(i, lo, hi, l, r):
            if l > hi or r < lo: return 0
            if lo >=l and hi <=r: return o.nl[i]
            m = (lo + hi)//2
            lt = query(i*2+1, lo, m, l, r)
            rt = query(i*2+2, m+1, hi, l, r)
            return lt + rt
        #print('sumRange ', o.nl)
        return query(0, 0, o.n-1, l, r)

obj = NumArray([1,2,3])
print(obj.sumRange(1,2))
obj.update(1,5)
print(obj.sumRange(1,2))
