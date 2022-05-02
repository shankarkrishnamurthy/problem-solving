class Solution:
    def minimumCardPickup(self, ca):
        ch, msf = {}, 100001
        for i in range(len(ca)):
            v = ca[i]
            if v in ch: msf = min(msf, i - ch[v][-1] + 1)
            ch.setdefault(v, []).append(i)
        return (msf if msf!=100001 else -1)
