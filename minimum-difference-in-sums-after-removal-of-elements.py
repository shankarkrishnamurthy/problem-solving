from heapq import *
class Solution:
    def minimumDifference(self, nums):
        n = len(nums)//3
        mih = list(map(lambda x:x*-1,nums[:n]))
        mis = [-sum(mih)]
        heapify(mih)
        for i in range(n,2*n):
            v = heappushpop(mih, -nums[i])
            mis.append(mis[-1]+nums[i] + v)
        mah = nums[2*n:]
        mas = [sum(mah)]
        heapify(mah)
        for i in range(2*n-1, n-1, -1):
            v = heappushpop(mah, nums[i])
            mas.append(mas[-1] + nums[i] - v)
        mas.reverse()
        #print(mis, mas)
        msf = mis[0] - mas[0]
        for a,b in zip(mis, mas):
            msf = min(msf, a-b)
        return msf
        
