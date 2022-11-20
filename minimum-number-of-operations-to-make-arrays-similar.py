class Solution:
    def makeSimilar(self, nums, target):
        ot, et, res, ei, oi = [], [], 0, 0, 0
        target.sort()
        for i in target:
            if i % 2 == 0: et.append(i)
            else: ot.append(i)
        nums.sort()
        for i in nums:
            if i % 2 == 0:
                if i < et[ei]: res += (et[ei] - i) // 2
                ei += 1
            else:
                if i < ot[oi]: res += (ot[oi] - i) // 2
                oi += 1
        return res
        
