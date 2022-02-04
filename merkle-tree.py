import hashlib as h
class Solution:
    def isSubtree(self, ro, sr):
        def dfs(r):
            if not r: return '#'
            d = bytes(dfs(r.left) + str(r.val) + dfs(r.right), 'utf-8')
            r.merkle = h.md5(d).hexdigest()
            return r.merkle
        dfs(ro)
        dfs(sr)
        def check(r):
            if not r: return False
            if r.merkle == sr.merkle: return True
            if check(r.left) or check(r.right): return True
            return False
        return check(ro)
