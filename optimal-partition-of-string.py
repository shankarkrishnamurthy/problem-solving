class Solution:
    def partitionString(self, s):
        dp,res = set(),1
        for v in s:
            if v in dp:
                dp = set([v])
                res += 1
                continue
            dp.add(v)
        return res
        
