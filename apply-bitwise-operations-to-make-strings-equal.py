class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        sc, tc = Counter(s), Counter(target)
        if tc["1"]==0 and sc["1"] == 0: return True
        if tc["1"]==0 or sc["1"] ==0: return False
        return True
