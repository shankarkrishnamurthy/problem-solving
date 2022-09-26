class Solution:
    def recoverArray(self, n, nums):
        def findone(arr, exc, inc):
            v, vh = arr[0] - arr[1], Counter(arr)
            for k in sorted(vh):
                while vh[k] > 0 and vh[k+v] > 0:
                    exc.append(k)
                    inc.append(k+v)
                    if v == 0: vh[k] -= 2
                    else: vh[k], vh[k+v] = vh[k]-1, vh[k+v]-1
            return v
        res = []
        nums.sort()
        while len(nums) > 1:
            inc, exc = [], []
            v = findone(nums, exc, inc)
            #print(nums,'excl ', exc,'incl ', inc, 'v', v)
            if 0 in inc: 
                res.append(-v)
                nums = inc
            else: 
                res.append(v)
                nums = exc
        return res
        
