class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            q = []
            for i in range(0,len(s),k):
                q.append(str(sum([int(s[j]) for j in range(i,min(len(s),i+k))])))
            #print (s, q)
            s = ''.join(q)
        return s
