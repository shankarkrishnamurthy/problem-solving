
class Solution:
    def recoverArray(self, nums):
        nums.sort()
        nh = {}
        [nh.setdefault(nums[i],[]).append(i) for i in range(len(nums))]
        def check(k,ans):
            s,vh=set(),{}
            for i,v in enumerate(nums):
                v1 = v+2*k
                vh[v]=vi=vh.get(v,0)
                vh[v1]=v1i=vh.get(v1,0)
                if vi >= len(nh[v]) or nh[v][vi] in s: continue
                if v1 not in nh: return False
                if v1i >= len(nh[v1]) or nh[v1][v1i] in s: return False
                s.add(nh[v][vi])
                s.add(nh[v1][v1i])
                vh[v] +=1
                vh[v1] += 1
                ans.append(v+k)
            if len(s) == len(nums): return True
            return False
        for i in range(1,(len(nums)//2)+1):
            k, ans = nums[0] + nums[i], []
            if (k) % 2 == 1: continue
            k = k//2 - nums[0]
            if k < 1: continue
            if check(k, ans): return ans
