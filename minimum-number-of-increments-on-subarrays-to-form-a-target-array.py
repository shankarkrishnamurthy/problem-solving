class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        pr, res = 0, 0
        for i in target:
            res += max(i - pr, 0)
            pr = i
        return res
