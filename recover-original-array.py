class Solution:
    def recoverArray(self, nums):
        nums.sort()
        nh = {}
        [nh.setdefault(nums[i],[]).append(i) for i in range(len(nums))]
        #print('nums ',nums)
        #print('nh ',nh)
        def check(k,ans):
            s,vh=set(),{}
            #print('check ', k)
            for i,v in enumerate(nums):
                v1 = v+2*k
                vh[v]=vi=vh.get(v,0)
                vh[v1]=v1i=vh.get(v1,0)
                if vi >= len(nh[v]) or nh[v][vi] in s: continue
                if v1 not in nh or v1i >= len(nh[v1]) or nh[v1][v1i] in s: return False
                s.add(nh[v][vi])
                s.add(nh[v1][v1i])
                vh[v], vh[v1] =vh[v]+1, vh[v1]+1
                ans.append(v+k)
                #print(' i,v', i,v,'set ', s)
            if len(s) == len(nums): return True
            return False
        for i in range(1,(len(nums)//2)+1):
            k, ans = nums[0] + nums[i], []
            if (k) % 2 == 1: continue
            k = k//2 - nums[0]
            if k < 1: continue
            if check(k, ans): return ans
        
print(Solution().recoverArray([36,67,13,17,14,63,69,21,45,79,8,72,64,48,23,34,58,58,76,17,14,42,58,76,94,6,46,10,98,65,39,55,88,46,32,18,18,65,79,35,59,2,14,61,4,54,68,48,41,50,26,100,80,30,92,52,30,19,2,22,96,75,100,62,83,96,62,44,45,26,41,6]))
print(Solution().recoverArray([2,10,6,4,8,12]))
print(Solution().recoverArray([5,435]))
print(Solution().recoverArray([1,1,3,3]))
print(Solution().recoverArray([11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]))
