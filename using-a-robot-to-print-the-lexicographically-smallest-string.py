class Solution:
    def robotWithString(self, s):
        res, t, ah, gi = [], [], defaultdict(list), 0
        for i, v in enumerate(s): ah[v].append(i)
        #print(dict(ah))
        for a in sorted(ah):
            ci = bisect_left(ah[a], gi)
            #print("gi", gi, 'current alphabet', a, 'ci', ci, 't', ''.join(t), 'res', ''.join(res))
            while t and t[-1] <= a: res.append(t.pop())
            for j in range(ci, len(ah[a])):
                i = ah[a][j]
                res.append(s[i])
                t += s[gi:i]
                gi = i+1
        while t: res.append(t.pop())
        return ''.join(res)
