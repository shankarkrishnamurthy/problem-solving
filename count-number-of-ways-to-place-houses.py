class Solution:
    def countHousePlacements(self,n):
        wo, wi, m  = 1, 1, 7+10**9
        for _ in range(n-1):
            wo, wi = (wo + wi) % m, wo
        return ((wo+wi)*(wo+wi)) % m
