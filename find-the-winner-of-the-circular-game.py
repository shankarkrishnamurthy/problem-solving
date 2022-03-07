class Solution:
    def findTheWinner(self, n, k):
        a,cnt,c = [],n,0
        for i in range(n):
            a.append(((i-1)% n,(i+1)%n))
        while cnt > 1:
            m = (k-1) % cnt
            while m > 0:
                c = a[c][1]
                m -= 1
            p,n = a[c]
            a[p] = (a[p][0],n)
            a[n] = (p,a[n][1])
            c = n
            cnt -= 1
        return c+1

print(Solution().findTheWinner(1,1))
print(Solution().findTheWinner(5,2))
print(Solution().findTheWinner(6,5))
