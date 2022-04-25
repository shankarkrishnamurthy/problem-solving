class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nh = Counter(nums)
        wo, wi , msf = {}, {}, 0
        print(sorted(nh))
        for i in sorted(nh):
            if i-1 in nh:
                wo[i] = wi[i-1]
                wi[i] = wo[i-1] + nh[i]*i
            else:
                wo[i] = msf
                wi[i] = msf + nh[i]*i
            msf = max(wo[i], wi[i])
            print((i), 'wo', wo, 'wi ', wi, 'msf ', msf)
        return msf


