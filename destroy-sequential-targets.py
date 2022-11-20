class Solution:
    def destroyTargets(self, nums, space):
        mh, sd, mac, mav = defaultdict(int), {}, 0, 0
        nums.sort()
        for i in nums:
            k = i%space
            if k not in mh: sd[k] = i
            mh[k] += 1
            if mh[k] > mac: mac, mav = mh[k], k
            if mh[k] == mac and sd[k] < sd[mav]: mac, mav = mh[k], k
        # print(nums)
        # print(dict(mh))
        # print(dict(sd))
        # print('mav', mav, 'mac', mac)
        return sd[mav]
