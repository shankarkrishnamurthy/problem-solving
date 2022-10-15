class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res, val, prev = [], 0, 0
        for i in pref:
            val = prev ^ i
            res.append(val)
            prev = i
            #print(val, i)
        return res
