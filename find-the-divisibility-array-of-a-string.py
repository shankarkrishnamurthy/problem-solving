class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res, v = [], 0
        for w in word:
            v = (v*10 + int(w)) % m
            res.append(int(v==0))
        return res
