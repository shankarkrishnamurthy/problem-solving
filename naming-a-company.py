class Solution:
    def distinctNames(self, ideas):
        ids, res = set(ideas), 0
        ccnt, avd = defaultdict(), defaultdict()
        for i in range(ord('a'), ord('z')+1):
            avd[chr(i)],ccnt[chr(i)] = defaultdict(), 0
            for j in range(ord('a'), ord('z')+1): avd[chr(i)][chr(j)] = 0
        for w in ideas:
            fc, ws = w[:1], w[1:]
            ccnt[fc] += 1
            for c in range(ord('a'), ord('z')+1):
                if fc == chr(c): continue
                if chr(c) + ws in ids: avd[chr(c)][fc] += 1
        for w in ideas:
            fc, ws = w[:1], w[1:]
            for c in range(ord('a'), ord('z')+1):
                if fc == chr(c): continue
                if chr(c) + ws not in ids:
                    res += (ccnt[chr(c)] - avd[chr(c)][fc])
        return res
