class Solution:
    def smallestNumber(self, pat):
        res = []
        def dfs(i, anc):
            nonlocal res
            if i == len(pat):
                res =  anc[::]
                return True
            for j in range(1,10):
                if pat[i] == "I" and anc[-1] >= j or j in anc: continue
                elif pat[i] == "D" and anc[-1] <= j or j in anc: continue
                if dfs(i+1, anc+[j]): return True
            return False
        for i in range(1,10):
            if dfs(0, [i]): break
        return ''.join(map(str, res))
        
