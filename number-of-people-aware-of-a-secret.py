class Solution:
    def peopleAwareOfSecret(self, n, d, f):
        shr, fgt, know, m = [0]*(n+1), [0]*(n+1), 1, 10**9+7
        for i in range(1,n+1):
            #print(i, 'know', know, 'share', shr, 'forget', fgt)
            ns = (shr[i] + know - fgt[i]) % m # number of guys who are active to share
            if i+d <=n: shr[i+d] = ns
            if i+f <=n: fgt[i+f] = ns
            know = ns
        return (know - fgt[n]) % m
