class Solution:
    def canChange(self, st, tgt):
        lp, rp, n, st, tgt = 0, len(tgt), len(tgt), list(st), list(tgt)
        tc, sc = Counter(st), Counter(tgt)
        if tc['L'] != sc['L'] or tc['R'] != sc['R']: return False
        for i in range(n):
            k, f = n-i-1, False
            if tgt[i] == 'L':
                j= max(i, lp)
                while j < len(st):
                    if st[j] == 'R': break
                    elif st[j] == '_': j += 1
                    else:
                        f, st[i], st[j], lp = True, st[j], st[i], j
                        break
            elif tgt[k] == 'R':
                j = min(k, rp)
                while j >=0:
                    if st[j] == 'L': break
                    elif st[j] == '_': j -= 1
                    else:
                        f, st[i], st[j], rp = True, st[j], st[i], j
                        break
            else: continue
            if not f: return False
        return True
            
        
