class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ct, res = Counter(tasks), 0
        for t in ct:
            if ct[t] % 3 == 0: res += ct[t]//3
            elif ct[t] % 3 == 2: res += ct[t]//3 + 1
            else:
                n = ct[t]//3
                if n > 0: res += n + 1
                else: return -1
        return res
